import logging
import sys
import os
from automation_script.enums.board_enums import JiraBoardConfig
from controllers.sprint_controller import SprintController
from services.sprint_service import SprintService
from services.jira_service import JiraService


def main():
    """Entry point for the sprint automation script.

    Parses arguments, validates the board, and runs the automation process.
    """
    try:
        board_name = sys.argv[1] if len(sys.argv) > 1 else os.getenv("BOARD")
        if not board_name:
            raise ValueError("No board specified for automation process.")

        try:
            board_config = JiraBoardConfig[board_name]
        except KeyError:
            valid_boards = [board.name for board in JiraBoardConfig]
            raise ValueError(
                f"Invalid board name: '{board_name}'. "
                f"Valid boards: {valid_boards}"
            )

        jira_service = JiraService()
        sprint_service = SprintService(jira_service.get_session())
        sprint_controller = SprintController(sprint_service)

        sprint_controller.automate_sprint(board_config)

    except SystemExit as e:
        logging.error(f"Script terminated: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()