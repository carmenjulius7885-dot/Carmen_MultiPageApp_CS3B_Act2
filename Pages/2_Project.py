import streamlit as st
import random

st.set_page_config(page_title="Game Hub", page_icon="🎮", layout="centered")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

.header {
    background: linear-gradient(90deg, #456882, #234C6A);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 0 25px rgba(0,114,255,0.6);
}

.card {
    background: #1e293b;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
    margin-bottom: 20px;
}

div.stButton > button {
    border-radius: 12px;
    background: #0ea5e9;
    color: white;
    font-weight: bold;
}

div.stButton > button:hover {
    background: #38bdf8;
    transform: scale(1.05);
    transition: 0.2s;
}

[data-baseweb="tab"] {
    font-size: 16px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <h1>💼My Project</h1>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["❌⭕ Tic Tac Toe", "✊✋✌️ Rock Paper Scissors"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("❌⭕ Tic Tac Toe")

    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
        st.session_state.winner = None

    def check_winner(board):
        combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
        for i,j,k in combos:
            if board[i] == board[j] == board[k] and board[i] != "":
                return board[i]
        if "" not in board:
            return "Draw"
        return None

    def ai_move():
        board = st.session_state.board
        empty = [i for i in range(9) if board[i] == ""]
        return random.choice(empty) if empty else None

    def make_move(i):
        if st.session_state.board[i] == "" and not st.session_state.winner:
            st.session_state.board[i] = "X"
            st.session_state.winner = check_winner(st.session_state.board)

            if not st.session_state.winner:
                ai = ai_move()
                if ai is not None:
                    st.session_state.board[ai] = "O"
                    st.session_state.winner = check_winner(st.session_state.board)

    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            i = row * 3 + col
            val = st.session_state.board[i]
            display = "❌" if val == "X" else "⭕" if val == "O" else " "
            with cols[col]:
                st.button(display, key=f"t{i}", on_click=make_move, args=(i,))

    if st.session_state.winner:
        if st.session_state.winner == "Draw":
            st.warning("😅 It's a Draw!")
        else:
            st.success(f"🏆 {st.session_state.winner} Wins!")

    if st.button("🔄 Restart"):
        st.session_state.board = [""] * 9
        st.session_state.winner = None
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✊✋✌️ Rock Paper Scissors")

    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
        st.session_state.computer_score = 0

    choices = ["Rock ✊", "Paper ✋", "Scissors ✌️"]
    user_choice = st.radio("Choose:", choices, horizontal=True)

    if st.button("🔥 Play"):
        computer_choice = random.choice(choices)

        col1, col2 = st.columns(2)
        col1.info(f"You: {user_choice}")
        col2.warning(f"Computer: {computer_choice}")

        if user_choice == computer_choice:
            st.write("🤝 Tie!")
        elif (
            ("Rock" in user_choice and "Scissors" in computer_choice) or
            ("Paper" in user_choice and "Rock" in computer_choice) or
            ("Scissors" in user_choice and "Paper" in computer_choice)
        ):
            st.success("🎉 You Win!")
            st.session_state.user_score += 1
        else:
            st.error("😢 You Lose!")
            st.session_state.computer_score += 1

    st.markdown("### 📊 Scoreboard")

    col1, col2 = st.columns(2)
    col1.metric("You", st.session_state.user_score)
    col2.metric("Computer", st.session_state.computer_score)

    if st.button("🔄 Reset Score"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
