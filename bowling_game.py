import logging

# Configure logging to show debug messages
logging.basicConfig(level=logging.DEBUG)

class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0
        logging.debug("Bowling game initialized.")

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        self.current_roll += 1
        logging.debug(f"Roll {self.current_roll}: {pins} pins.")

    def score(self):
        score = 0
        frame_index = 0

        for frame in range(10):
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                logging.debug(f"Frame {frame + 1} (Strike): Total score so far: {score}")
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                logging.debug(f"Frame {frame + 1} (Spare): Total score so far: {score}")
                frame_index += 2
            else:
                # Open frame
                score += self.rolls[frame_index]
                logging.debug(f"Frame {frame + 1} (Open): Total score so far: {score}")
                frame_index += 2

        logging.debug(f"Final score: {score}")
        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        result = frame_index < len(self.rolls) and self.rolls[frame_index] == 10
        logging.debug(f"Frame {frame_index + 1} is Strike: {result}")
        return result

    def _is_spare(self, frame_index):
        """
        Check if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        result = frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        logging.debug(f"Frame {frame_index + 1} is Spare: {result}")
        return result

    def _strike_bonus(self, frame_index):
        bonus = 0
        if frame_index + 1 < len(self.rolls):
            bonus += self.rolls[frame_index + 1]
        if frame_index + 2 < len(self.rolls):
            bonus += self.rolls[frame_index + 2]

        logging.debug(f"Strike bonus for frame {frame_index + 1}: {bonus}")
        return bonus


    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        bonus = self.rolls[frame_index + 2]
        logging.debug(f"Spare bonus for frame {frame_index + 1}: {bonus}")
        return bonus
