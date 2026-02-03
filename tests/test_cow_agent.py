"""Tests for animal_counter."""

from animal_counter import CowAgent
from code_puppy.agents.base_agent import BaseAgent


def test_is_base_agent():
    assert isinstance(CowAgent(), BaseAgent)


def test_has_image_tool():
    assert "load_image_for_analysis" in CowAgent().get_available_tools()


def test_model():
    assert CowAgent().get_model_name() == "claude-4-5-sonnet"


def test_prompt_loaded():
    assert "opencv" in CowAgent().get_system_prompt().lower()
