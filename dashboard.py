import streamlit as st
import plotly.express as px
import pandas as pd
from database import get_all_sessions
from coach import get_coach_feedback

def show_dashboard():
    st.subheader("Session History")

    sessions = get_all_sessions()
    if not sessions:
        st.info("No sessions yet — start a session to see your stats!")
        return

    # Convert to dataframe
    df = pd.DataFrame(sessions, columns=[
        "id", "date", "duration_seconds", 
        "focused_pct", "confused_pct", "distracted_pct"
    ])
    df["duration_mins"] = round(df["duration_seconds"] / 60, 1)

    # Summary metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sessions", len(df))
    col2.metric("Avg Focus", f"{round(df['focused_pct'].mean(), 1)}%")
    col3.metric("Total Study Time", f"{round(df['duration_mins'].sum(), 1)} mins")

    # Focus trend chart
    fig = px.line(df, x="date", y="focused_pct",
                  title="Focus % Over Time",
                  labels={"focused_pct": "Focused %", "date": "Session Date"},
                  markers=True)
    fig.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

    # State breakdown bar chart
    latest = df.iloc[0]
    fig2 = px.bar(
        x=["Focused", "Confused", "Distracted"],
        y=[latest["focused_pct"], latest["confused_pct"], latest["distracted_pct"]],
        title="Latest Session Breakdown",
        labels={"x": "State", "y": "Percentage"},
        color=["Focused", "Confused", "Distracted"],
        color_discrete_map={
            "Focused":"#00C851",
            "Confused": "#FF8800",
            "Distracted": "#FF4444"
        }
    )
    st.plotly_chart(fig2, use_container_width=True)

    # LLM Coach feedback
    st.subheader("AI Study Coach")
    if st.button("Get Coaching Feedback"):
        with st.spinner("Coach is analysing your session..."):
            feedback = get_coach_feedback(
                duration=int(latest["duration_seconds"]),
                focused=latest["focused_pct"],
                confused=latest["confused_pct"],
                distracted=latest["distracted_pct"]
            )
        st.success(feedback)
