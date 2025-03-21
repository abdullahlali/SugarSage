import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup")
class TestSugarSageWebsite:
    def setup_method(self):
        """Setup method that runs before each test"""
        self.driver.get("https://abdullahlali.github.io/SugarSage/")
        
    def test_diabetes_prediction(self):
        """Test if the diabetes prediction form is functional"""
        try:
            # Wait for the prediction form to be visible
            form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "prediction-form"))
            )
            
            # Test filling out the form using name attributes
            gender_field = self.driver.find_element(By.NAME, "gender")
            age_field = self.driver.find_element(By.NAME, "age")
            hypertension_field = self.driver.find_element(By.NAME, "hypertension")
            heart_disease_field = self.driver.find_element(By.NAME, "heart_disease")
            smoking_history_field = self.driver.find_element(By.NAME, "smoking_history")
            bmi_field = self.driver.find_element(By.NAME, "bmi")
            hba1c_level_field = self.driver.find_element(By.NAME, "HbA1c_level")
            glucose_level_field = self.driver.find_element(By.NAME, "blood_glucose_level")
            
            # Fill out the form fields with sample data
            select_gender = Select(gender_field)
            select_gender.select_by_value("1")  # Male
            
            age_field.send_keys("30")
            select_hypertension = Select(hypertension_field)
            select_hypertension.select_by_value("1")  # Yes
            
            select_heart_disease = Select(heart_disease_field)
            select_heart_disease.select_by_value("1")  # Yes
            
            select_smoking_history = Select(smoking_history_field)
            select_smoking_history.select_by_value("3")  # Current Smoker
            
            bmi_field.send_keys("25.5")
            hba1c_level_field.send_keys("6.5")
            glucose_level_field.send_keys("120")
            
            # Check that the form fields are filled correctly
            assert select_gender.first_selected_option.get_attribute("value") == "1"
            assert age_field.get_attribute("value") == "30"
            assert select_hypertension.first_selected_option.get_attribute("value") == "1"
            assert select_heart_disease.first_selected_option.get_attribute("value") == "1"
            assert select_smoking_history.first_selected_option.get_attribute("value") == "3"
            assert bmi_field.get_attribute("value") == "25.5"
            assert hba1c_level_field.get_attribute("value") == "6.5"
            assert glucose_level_field.get_attribute("value") == "120"
            
            # Wait for the Predict button to be clickable
            predict_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "predict-button"))
            )
            
            # Scroll the button into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", predict_button)
            
            # Click the Predict button using JavaScript
            self.driver.execute_script("arguments[0].click();", predict_button)
            
            # Wait for the prediction result section to be visible
            result_section = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "prediction-result-section"))
            )
            
            # Check if the result section is displayed
            assert result_section.is_displayed()
            
            # Check if the prediction percentage text is shown
            prediction_percentage = self.driver.find_element(By.ID, "prediction-percentage")
            assert prediction_percentage is not None
            assert "Probability: " in prediction_percentage.text
            
            # Check if the "Fill another form?" button is displayed
            fill_another_button = self.driver.find_element(By.ID, "fill-another-form")
            assert fill_another_button.is_displayed()

        except Exception as e:
            pytest.fail(f"Prediction form test failed: {str(e)}")
            
    def test_page_title(self):
        """Test if the page title is correct"""
        assert "SugarSage" in self.driver.title
        
    def test_navigation(self):
        """Test if main navigation elements are present"""
        nav_elements = self.driver.find_elements(By.TAG_NAME, "nav")
        assert len(nav_elements) == 0
            
    def test_chatbot_response(self):
        """Test if the chatbot is receiving and responding correctly"""
        try:
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.execute_script('return document.readyState') == 'complete'
            )

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait for the input field to be present and visible
            user_input_field = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.ID, "user-input"))
            )
            
            # Wait for the send button to be clickable
            send_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, "send-button"))
            )

            # Simulate entering a question and clicking send
            user_input_field.send_keys("What is diabetes?")
            send_button.click()

            # Wait for the chatbot's response to appear in the chatbox
            chatbox = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "chatbox"))
            )

            # Check if the chatbox has received a response and it's not the default welcome message
            assert chatbox.text != "SugarSage: Welcome! Ask me anything about diabetes or related information."

        except Exception as e:
            # Print the page source for debugging if the test fails
            pytest.fail(f"Chatbot test failed: {str(e)}")


            
    def test_responsive_design(self):
        """Test if the website is responsive"""
        # Test mobile viewport
        self.driver.set_window_size(375, 812)  # iPhone X dimensions
        assert self.driver.find_element(By.TAG_NAME, "body").is_displayed()
        
        # Test tablet viewport
        self.driver.set_window_size(768, 1024)  # iPad dimensions
        assert self.driver.find_element(By.TAG_NAME, "body").is_displayed()
        
        # Test desktop viewport
        self.driver.set_window_size(1920, 1080)  # Full HD
        assert self.driver.find_element(By.TAG_NAME, "body").is_displayed()

    def test_go_to_chatbot_button(self):
        """Test if the 'Go to Chatbot' button scrolls to the chatbot section"""
        try:
            # Locate the button and the chatbot section
            button = self.driver.find_element(By.ID, "go-to-chatbot")  # Adjust the ID as needed
            chatbot_section = self.driver.find_element(By.ID, "chatbot-section")  # Adjust the ID as needed

            # Click the button using JavaScript (more reliable)
            self.driver.execute_script("arguments[0].click();", button)

            # Explicitly wait for the chatbot section to become visible
            WebDriverWait(self.driver, 10).until(EC.visibility_of(chatbot_section))

            # (Optional) Debugging delay to check if it's a timing issue
            time.sleep(2)  

            # Verify the chatbot section is displayed
            assert chatbot_section.is_displayed()

        except Exception as e:
            pytest.fail(f"Go to Chatbot button test failed: {str(e)}")

    def test_smooth_scroll_back_to_top(self):
        """Test if the 'Back to Top' button smoothly scrolls to the top of the page"""
        try:
            # Scroll down first to ensure the button is visible
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Allow some time for the scroll to complete

            # Locate the 'Back to Top' button
            back_to_top_button = self.driver.find_element(By.ID, "back-to-top")  # Adjust ID if needed

            # Click the button
            self.driver.execute_script("arguments[0].click();", back_to_top_button)

            # Wait for the page to scroll to the top
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script("return window.scrollY") == 0
            )

            # Verify we are at the top of the page
            assert self.driver.execute_script("return window.scrollY") == 0

        except Exception as e:
            pytest.fail(f"Smooth scroll with Back to Top button failed: {str(e)}")


if __name__ == "__main__":
    pytest.main() 