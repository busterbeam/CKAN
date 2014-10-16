// Communicate with the user (status messages, yes/no questions, etc)
// This class will proxy to either the GUI or cmdline functionality.

namespace CKAN {
    using System;

    public class User {

        public static bool noConsole = false;

        // Send a line to the user. On a console, this does what you expect.
        // In the GUI, this should update the status bar.
        // This is also an obvious place to do logging as well.
        public static void WriteLine(string text, params object[] args) {

            // Format our message.
            string message = String.Format (text, args);

            // Right now we always send to the console, but when we add extra
            // interfaces we'll switch to the appropriate one here.
            Console.WriteLine (message);
        }

        /// <summary>
        /// Prompts the user for a Y/N response.
        /// Returns true for yes, false for no.
        /// </summary>

        public static bool YesNo(string text = null) {

            if (noConsole)
            {
                return true;
            }

            if (text != null) {
                User.WriteLine ("{0} [Y/N]", text);
            }

            while (true) {
                ConsoleKeyInfo keypress = Console.ReadKey(true);

                if (keypress.Key == ConsoleKey.Y) {
                    return true;
                }
                else if (keypress.Key == ConsoleKey.N) {
                    return false;
                }

                // TODO: Can we end up in an infinite loop here?
                // What if the console disappears or something?
            }
        }
    }
}

