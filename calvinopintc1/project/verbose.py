# ======================
# Global verbose toggle
# ======================

# ANSI color codes
YELLOW = "\033[93m" # ANSI escape sequence for yellow text
RESET = "\033[0m"   # ANSI escape sequence to reset text color

def verbose_log(message):
    """Prints a colored verbose message if verbose mode is enabled."""
    if VERBOSE_MODE_ENABLED:
        print(f"{YELLOW}[VERBOSE] {message}{RESET}")

def set_verbose(enabled: bool):
    """Enable or disable verbose logging globally."""
    global VERBOSE_MODE_ENABLED
    VERBOSE_MODE_ENABLED = enabled
