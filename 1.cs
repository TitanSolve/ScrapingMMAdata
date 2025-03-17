using System;
using System.Threading;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.DevTools;

class Program
{
    static void Main()
    {
        // Set Chrome options for "undetected" behavior
        ChromeOptions options = new ChromeOptions();
        options.AddArgument("--disable-blink-features=AutomationControlled"); // Helps evade detection
        options.AddExcludedArgument("enable-automation"); // Removes "controlled by automation"
        options.AddAdditionalOption("useAutomationExtension", false);
        options.AddArgument("--start-maximized"); // Open in full screen
        options.AddArgument("--disable-popup-blocking"); // Disable popup blockers

        // Start ChromeDriver with options
        using (IWebDriver driver = new ChromeDriver(options))
        {
            // Activate Chrome DevTools Protocol (CDP)
            var devTools = ((ChromeDriver)driver).GetDevToolsSession();
            devTools.SendCommand("Page.enable", new { }); // Enable DevTools

            // Navigate to the bot detection page
            driver.Navigate().GoToUrl("https://www.browserscan.net/bot-detection");

            // Keep browser open for inspection
            Console.WriteLine("Press Enter to close the browser...");
            Console.ReadLine();
        }
    }
}
