cat > omega_llm.py << 'EOF'
import requests
from omega_config import OPENROUTER_API_KEY, OPENROUTER_URL, MODEL
from omega_prompt import SYSTEM_PROMPT

def ask_llm(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT + """

CRITICAL EXECUTION RULES:
- You MUST complete the entire response in one continuous output
- Never stop mid-code or mid-explanation
- If writing scripts, ALWAYS finish full runnable programs
- Do NOT switch topics mid-response
- Treat each request as a single atomic task that must be fully completed
"""},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
        "max_tokens": 3000
    }

    r = requests.post(OPENROUTER_URL, headers=headers, json=payload)

    try:
        return r.json()["choices"][0]["message"]["content"]
    except:
        return "Omega AI error: invalid response"
EOF
