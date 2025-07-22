from api_utils import analyze_with_llm
from prompt_utils import load_prompt, format_prompt
import os
import re
import json


def extract_json_from_response(response_text):
    """
    Витягує JSON-блок із LLM-відповіді (видаляє ```json ... ``` якщо потрібно).
    """
    # Шукаємо блок між ```json і ```
    json_match = re.search(r'```json\s*({.*?})\s*```', response_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
    else:
        # Якщо немає markdown, шукаємо просто { ... }
        json_match = re.search(r'({.*})', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            raise ValueError("Не знайдено JSON у відповіді LLM")
    return json.loads(json_str)


# --- Complaint Handling and Escalation ---
PROMPT_PATH_COMPLAINT = os.path.join("prompts", "complaint_handling.txt")
PROMPT_TEMPLATE_COMPLAINT = load_prompt(PROMPT_PATH_COMPLAINT)

def check_complaint_handling(text, complaint_flag=None):
    """
    Перевіряє наявність скарги у транскрипції та чи була вона відмічена представником.
    Використовує LLM-промпт з complaint_flag.
    """
    flag_value = complaint_flag if complaint_flag is not None else "unknown"
    prompt = format_prompt(
        PROMPT_TEMPLATE_COMPLAINT,
        transcription=text,
        complaint_flag=flag_value
    )
    response = analyze_with_llm(prompt)
    try:
        llm_json = extract_json_from_response(response)
        complaint_detected = llm_json.get("complaint_detected")
        flagged = llm_json.get("flagged_by_representative")
        violation = llm_json.get("violation")
        reason = llm_json.get("reason")
    except Exception as e:
        complaint_detected = None
        flagged = None
        violation = None
        reason = f"Parse error: {str(e)}"
    return {
        "complaint_detected": complaint_detected,
        "flagged_by_representative": flagged,
        "violation": violation,
        "reason": reason,
        "raw_response": response
    }


# --- Call Recording Disclosure ---
PROMPT_PATH_RECORDING = os.path.join("prompts", "call_recording_disclosure.txt")
PROMPT_TEMPLATE_RECORDING = load_prompt(PROMPT_PATH_RECORDING)

def check_call_recording_disclosure(text):
    """
    Перевірка, чи попередив агент про запис розмови.
    """
    prompt = format_prompt(
        PROMPT_TEMPLATE_RECORDING,
        transcription=text
    )
    response = analyze_with_llm(prompt)
    try:
        llm_json = extract_json_from_response(response)
        disclosure_detected = llm_json.get("disclosure_detected")
        violation = llm_json.get("violation")
        reason = llm_json.get("reason")
    except Exception as e:
        disclosure_detected = None
        violation = None
        reason = f"Parse error: {str(e)}"
    return {
        "disclosure_detected": disclosure_detected,
        "violation": violation,
        "reason": reason,
        "raw_response": response
    }


# --- Aggressive or Pressuring Selling Language ---
PROMPT_PATH_MARKETING = os.path.join("prompts", "aggressive_marketing.txt")
PROMPT_TEMPLATE_MARKETING = load_prompt(PROMPT_PATH_MARKETING)

def check_aggressive_marketing(text):
    """
    Виявлення агресивних/оманливих формулювань у маркетингових матеріалах.
    """
    prompt = format_prompt(
        PROMPT_TEMPLATE_MARKETING,
        transcription=text
    )
    response = analyze_with_llm(prompt)
    try:
        llm_json = extract_json_from_response(response)
        aggressive_language_detected = llm_json.get("aggressive_language_detected")
        violation = llm_json.get("violation")
        reason = llm_json.get("reason")
    except Exception as e:
        aggressive_language_detected = None
        violation = None
        reason = f"Parse error: {str(e)}"
    return {
        "aggressive_language_detected": aggressive_language_detected,
        "violation": violation,
        "reason": reason,
        "raw_response": response
    }