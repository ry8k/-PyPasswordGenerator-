# 🔒 Password Generator Project ✨

Create secure and customizable passwords effortlessly with this Python-based Password Generator! 🚀

## 🛠 Features

- **Customizable Lengths** 🔢
  - Choose the number of **letters**, **symbols**, and **numbers** in your password.
  
- **Randomization** 🎲
  - **Hard Level**: Characters are shuffled for enhanced security.
  
- **User-Friendly** 😊
  - Interactive prompts guide you through password creation.
  - Error handling ensures valid inputs.

## 📚 How It Works

1. **Imports Required Modules** 🐍
   ```py
   import random
   ```
   
2. **Defines Character Pools** 🔠🔢🔣
   - **Letters**: a-z, A-Z
   - **Numbers**: 0-9
   - **Symbols**: `! # $ % & ( ) * +`
   
3. **Handles User Input** 📝
   - Prompts for the number of letters, symbols, and numbers.
   - Validates inputs to ensure they are numbers and not zero.
   
4. **Generates Password Components** 🛡
   - Randomly selects the specified number of letters, symbols, and numbers.
   
5. **Shuffles Characters** 🔀
   - Combines all characters and shuffles them to create a secure password.
   
6. **Displays the Final Password** 🗝️
   - Outputs the generated password to the user.

## 📥 Usage

1. **Run the Script** 🖥️
   ```bash
   python main.py
   ```
   
2. **Follow the Prompts** 🗯️
   - Enter the desired number of letters, symbols, and numbers.
   
3. **Receive Your Password** 🎉
   - View and use your securely generated password.

## 📊 Example

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
4
How many symbols would you like?
2
How many numbers would you like?
2
Your password is : g^2jk8&P
Press enter to exit.
```

## 🧰 Technologies Used

- **Python** 🐍
  - Utilizes the `random` module for generating random characters.

## 🛡 Security Considerations

- Ensures passwords are not predictable by randomizing character order.
- Validates user input to prevent errors and ensure password integrity.

---

Feel free to contribute or raise issues! Happy coding! 💻🔐
