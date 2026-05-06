cat > omega_router.py << 'EOF'
from omega_llm import ask_llm
from omega_ui_renderer import render

def route(user_text):
    response = ask_llm(user_text)

    explanation = response
    code = None
    command = None

    # detect code blocks
    if "```" in response:
        parts = response.split("```")

        explanation = parts[0].strip()

        if len(parts) > 1:
            code = parts[1].replace("python", "").strip()

    return render(explanation, code, command)
EOF
