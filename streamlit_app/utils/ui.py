import pandas as pd
import streamlit as st


def header_description():
    st.title("Food Classification :pizza::meat_on_bone::sushi:")
    st.image("static/food.jpg")
    st.write(
        """
        This project is an AI tool based on CNN to classify types of food **(sushi, pizza, steak)**.
        This project is based on CNN with the transfer learning method (using efficient-net).
        """
    )


def result(output):
    st.subheader("Result")

    output_json = output.json()
    output_json["probability"] = str(round(output_json["probability"], 4) * 100) + " %"
    output_json["execution_time"] = str(round(output_json["execution_time"], 3)) + " s"

    df = pd.DataFrame(
        {
            "Output": ["predict_label", "probability", "execution_time"],
            "Value": [
                output_json["predict_label"],
                output_json["probability"],
                output_json["execution_time"],
            ],
        }
    )

    return st.dataframe(df, width=250, hide_index=True)


def sidebar() -> None:
    with st.sidebar:
        st.header("Food Classification")
