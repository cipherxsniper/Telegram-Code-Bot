cat > omega_ui_renderer.py << 'EOF'
def render(explanation=None, code=None, command=None):
    output = ""

    # 🧠 Explanation block
    if explanation:
        output += f"{explanation}\n\n"

    # 💻 Code block (ONLY CODE INSIDE)
    if code:
        output += "```python\n"
        output += code.strip()
        output += "\n```\n\n"

    # ⚡ Command block (TERMUX SAFE)
    if command:
        output += "```bash\n"
        output += command.strip()
        output += "\n```\n\n"

    return output
EOF
