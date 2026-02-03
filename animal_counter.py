#!/usr/bin/env python3
"""🐄👁️ Bessie the CV Cow - Requires ANTHROPIC_API_KEY environment variable."""

import asyncio
import sys
from pathlib import Path
from code_puppy.agents.base_agent import BaseAgent
from code_puppy.tools.common import console

PROMPT = (Path(__file__).parent / "cow_prompt.md").read_text()


class CowAgent(BaseAgent):
    name = "cow-agent"
    display_name = "🐄👁️ Bessie the CV Cow"
    description = "OpenCV expert that counts animals in images"

    def get_model_name(self):
        return "claude-4-5-sonnet"

    def get_system_prompt(self):
        return PROMPT

    def get_available_tools(self):
        return [
            "load_image_for_analysis",
            "list_files",
            "read_file",
            "edit_file",
            "agent_run_shell_command",
            "agent_share_your_reasoning",
        ]


async def main():
    console.print(
        "[bold cyan]🐄👁️ Bessie the CV Cow[/bold cyan] [dim](claude-sonnet-4-5)[/dim]\n"
    )
    cow = CowAgent()

    if len(sys.argv) > 1:
        console.print(f"[green]You:[/green] {' '.join(sys.argv[1:])}\n")
        r = await cow.run_with_mcp(" ".join(sys.argv[1:]))
        console.print(
            f"\n[yellow]Bessie:[/yellow] {r.data if hasattr(r, 'data') else r}\n"
        )
    else:
        console.print("[dim]Interactive mode. 'quit' to exit.[/dim]\n")
        while True:
            try:
                p = input("Prompt (example: Count elk in Elk-Count.jpg) >>> ").strip()
                if not p:
                    continue
                if p.lower() in ("quit", "exit", "q"):
                    break
                if p.lower() == "clear":
                    cow.clear_message_history()
                    console.print("[dim]Cleared.[/dim]")
                    continue
                r = await cow.run_with_mcp(p)
                console.print(
                    f"\n[yellow]Bessie:[/yellow] {r.data if hasattr(r, 'data') else r}\n"
                )
            except (KeyboardInterrupt, EOFError):
                break
        console.print("[yellow]🐄 Moo! Bye![/yellow]")


def cli_main():
    asyncio.run(main())


if __name__ == "__main__":
    cli_main()
