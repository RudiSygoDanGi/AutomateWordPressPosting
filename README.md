# Playwright WordPress Auto Post

This script uses Playwright, a Python library for automating browser actions, to log in to a WordPress website and create a new post with a featured image.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your machine
- The Playwright library installed (`pip install playwright`)
- The necessary credentials for logging in to your WordPress website

## Installation

1. Clone this repository or download the script file.
2. Install the required dependencies by running the following command:

   ```
   pip install playwright
   ```

## Configuration

1. Open the script file in a text editor.
2. Replace `'YourUsername'` with your WordPress username.
3. Replace `'YourPassword'` with your WordPress password.
4. Customize the post details by modifying the `title`, `content`, and `image_path` variables.

## Usage

To run the script, execute the following command:

```
python your_script_name.py
```

Replace `your_script_name.py` with the actual name of the script file.

## Script Explanation

The script performs the following actions:

1. Launches a new browser instance using Playwright.
2. Creates a new browser context.
3. Navigates to the WordPress login page.
4. Fills in the login form and submits it.
5. Waits for the WordPress dashboard to load.
6. Navigates to the Posts page.
7. Clicks the "Add New" button to create a new post.
8. Fills in the post title and content.
9. Uploads the featured image for the post.
10. Publishes the post.
11. Waits for the post to be published and navigates to the post page.
12. Closes the browser context and exits the script.

Note: The script assumes that the necessary selectors and elements exist on the WordPress website. If any changes are made to the WordPress website structure or elements, the script may need to be updated accordingly.

Feel free to customize the script further based on your specific requirements. Happy automating!
