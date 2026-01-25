from langchain_core.messages import HumanMessage, AIMessage
from src.agents.coffee_agent import agent
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class CoffeePlanner:
    def __init__(self):
        self.messages = []
        logger.info("CoffeePlanner initialized")

    def create_recipe(
        self,
        coffee_type: str,
        strength: int,
        flavors: list[str],
        milk: str,
        sweetness: str,
        temperature: str
    ):
        try:
            user_prompt = f"""
            Create a personalized coffee recipe.

            Coffee Type: {coffee_type}
            Strength Level: {strength}/5
            Flavor Preferences: {', '.join(flavors)}
            Milk Type: {milk}
            Sweetness Level: {sweetness}
            Temperature: {temperature}

            Provide:
            - Ingredients with measurements
            - Step-by-step preparation method
            - Brewing tips and barista recommendations
            """

            self.messages.append(HumanMessage(content=user_prompt))

            response = agent.invoke({
                "messages": self.messages
            })

            final_answer = response["messages"][-1].content
            self.messages.append(AIMessage(content=final_answer))

            return final_answer

        except Exception as e:
            logger.error(f"CoffeePlanner error: {e}")
            raise CustomException("Failed to generate coffee recipe", e)
