"""
The Chat Page:
Here, users will be able to interact with ELIZA. The page should simulate a conversation using pattern matching and substitutions.
"""
import streamlit as st
import re
import random
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional

@dataclass
class ToyotaModel:
    name: str
    base_price: float
    available_colors: List[str]
    features: List[str]
    body_type: str

@dataclass
class ChatPattern:
    pattern: str
    responses: List[str]
    requires_context: bool = False
    
    def match(self, text: str) -> Optional[re.Match]:
        return re.match(self.pattern, text.lower())

class ToyotaSalesBot:
    def __init__(self):
        self.models = {
            'rav4': ToyotaModel(
                name='RAV4',
                base_price=27_475,
                available_colors=['Red', 'Blue', 'Black', 'Silver', 'White', 'Gray'],
                features=['All-Wheel Drive', 'Toyota Safety Sense 2.0', 'Apple CarPlay'],
                body_type='SUV'
            ),
            'corolla': ToyotaModel(
                name='Corolla',
                base_price=21_550,
                available_colors=['Red', 'Blue', 'Black', 'White', 'Silver'],
                features=['Lane Departure Alert', 'Dynamic Radar Cruise Control'],
                body_type='Sedan'
            )
        }
        
        self.conversation_context = {
            'current_model': None,
            'mentioned_features': set(),
            'price_range': None
        }
        
        self.patterns = [
            ChatPattern(
                r"hi|hello|hey",
                [
                    "Welcome to Toyota Sales! I'm Joe Girard. Are you looking for a specific type of vehicle?",
                    "Hello! I'm Joe, your Toyota specialist. What brings you in today?"
                ]
            ),
            ChatPattern(
                r"i'm looking for (.*)",
                [
                    "I can help you find {0}! Our {available_models} might be perfect for your needs. "
                    "What's your preferred body style - sedan or SUV?"
                ],
                requires_context=True
            ),
            ChatPattern(
                r"budget.*?(\d{4,6})",
                [
                    "With a budget of ${0}, I'd recommend the {recommended_models}. "
                    "Would you like to explore any of these options?"
                ],
                requires_context=True
            )
        ]

    def get_available_models(self) -> str:
        return ", ".join([f"{model.name} (starting at ${model.base_price:,})" 
                         for model in self.models.values()])

    def get_recommended_models(self, budget: float) -> List[str]:
        if budget is None:
            return ["No budget specified."]
        return [model.name for model in self.models.values() 
                if model.base_price <= budget]

    def update_context(self, user_input: str) -> None:
        for model_name in self.models:
            if model_name in user_input.lower():
                self.conversation_context['current_model'] = self.models[model_name]
                break
        
        price_match = re.search(r'\$?(\d{4,6})', user_input)
        if price_match:
            self.conversation_context['price_range'] = float(price_match.group(1))

    def generate_response(self, user_input: str) -> str:
        self.update_context(user_input)
        
        for pattern in self.patterns:
            match = pattern.match(user_input)
            if match:
                response = random.choice(pattern.responses)
                
                if pattern.requires_context:
                    response = response.format(
                        *match.groups(),
                        available_models=self.get_available_models(),
                        recommended_models=", ".join(
                            self.get_recommended_models(
                                self.conversation_context.get('price_range', float('inf'))
                            )
                        )
                    )
                return response
        
        return "I'd be happy to help you find the perfect Toyota. Could you tell me more about what you're looking for?"

def run_chatbot():
    st.title("Joe Girard - Your Personal Toyota Specialist")
    st.write("Welcome! I'm here to help you find your perfect Toyota. With over 40 years of experience, "
             "I've helped thousands of customers drive home happy.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.bot = ToyotaSalesBot()

    st.header("Chat with Joe")
    user_input = st.chat_input(placeholder="Tell me what you're looking for in your next car...")

    if user_input:
        response = st.session_state.bot.generate_response(user_input)
        st.session_state.chat_history.append((user_input, response))

    for user_msg, joe_response in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(user_msg)
        with st.chat_message("assistant"):
            st.markdown(joe_response)

#if __name__ == "__main__":
    run_chatbot()
