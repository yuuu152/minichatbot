import tkinter as tk
from tkinter import scrolledtext

# 🧠 Your basic knowledge bank
knowledge = {
    "hello": "Hello there! How can I help you today?",
    "bye": "bye sweetie ^^",
    "find value of integration (xsq - 1)/(xsq+1) * (1)/(wholesqrt 1+x to the power 4)": (
        "Let's solve the integral step-by-step:\n\n"
        "∫ [(x² - 1)/(x² + 1)] · [1/√(1 + x⁴)] dx\n\n"
        "Step 1: Check for symmetry — plug in -x:\n"
        "      f(-x) = f(x) ⇒ the function is even, not odd.\n\n"
        "Step 2: Use substitution x = 1/t ⇒ dx = -1/t² dt\n"
        "      Then x² = 1/t², x⁴ = 1/t⁴\n"
        "      Rewrite the expression:\n"
        "      ∫ [(1 - t²)/(1 + t²)] · [1/√(1 + 1/t⁴)] · (-1/t²) dt\n\n"
        "Step 3: Simplify:\n"
        "      √(1 + 1/t⁴) = √((t⁴ + 1)/t⁴) = √(t⁴ + 1) / t²\n"
        "      So full expression becomes:\n"
        "      -∫ [(1 - t²)/(1 + t²)] · [1/√(t⁴ + 1)] dt\n\n"
        "Step 4: You now get:\n"
        "      I = -I ⇒ 2I = 0 ⇒ I = 0\n\n"
        "✅ Final Answer: 0"
    ),
    "who is dhruba" : "my owner",
    
}

# 🧠 Reply logic with keyword search
def get_bot_response(user_input):
    user_input = user_input.lower()

    for question in knowledge:
        if question in user_input:
            return knowledge[question]

    return "Sorry, I don't know that yet. I'm still learning!"

# 📤 Send button function
def send_message(event=None):
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_msg + "\n")

    bot_reply = get_bot_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    chat_area.config(state=tk.DISABLED)

    chat_area.yview(tk.END)
    user_input.delete(0, tk.END)

# 🖥️ GUI Setup
root = tk.Tk()
root.title("Offline SmartBot")
root.geometry("500x600")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input = tk.Entry(root, font=("Arial", 12))
user_input.pack(padx=10, pady=(0,10), fill=tk.X)
user_input.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=(0, 10))

root.mainloop()


