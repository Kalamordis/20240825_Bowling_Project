import logging

logging.basicConfig(level=logging.DEBUG)

class BowlingGame:
    """ 
    This code is for a bowling game, managing the roll history and score calculation.

    Attributes:
        rolls (list): A list of how many pins were knocked down during each roll.
        current_roll (int): An index that points to the current roll.
    """
    
    def __init__(self):
        """ 
        Initializes a new BowlingGame instance, meaning it has an empty roll history 
        and resets the current roll index to 0.
        """
        self.rolls = []
        self.current_roll = 0
        logging.debug("Bowling game initialized.")

    def roll(self, pins):
        """ 
        Records the rolls throughout the game.
        
        Args:
            pins (int): The number of pins knocked down in the roll that is currently being rolled.
        
        Puts the roll in the log, and then increments the roll counter for the next roll.
        """
        self.rolls.append(pins)
        self.current_roll += 1
        logging.debug(f"Roll {self.current_roll}: {pins} pins.")

    def score(self):
        """ 
        Calculates and returns the total score for the game.
        
        The score is calculated across the entirety of the 10 frames. Each frame consists 
        of a maximum of two rolls, with the exception of the 10th frame, which can contain 
        up to three rolls, depending on if a strike or spare has occurred.
        
        Returns:
            int: The total score for the game.
        """
        score = 0
        frame_index = 0

        for frame in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                logging.debug(f"Frame {frame + 1} (Strike): Total score so far: {score}")
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                logging.debug(f"Frame {frame + 1} (Spare): Total score so far: {score}")
                frame_index += 2
            else:
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                logging.debug(f"Frame {frame + 1} (Open): Total score so far: {score}")
                frame_index += 2

        logging.debug(f"Final score: {score}")
        return score

    def _is_strike(self, frame_index):
        """ 
        Checks if the roll at frame_index is a strike or not (A strike requires 10 pins to be knocked down.)
        
        Args: 
            frame_index (int): The index of the roll that is checked
        
        Returns:
            bool: True if the roll is a strike, else False.
        """
        result = frame_index < len(self.rolls) and self.rolls[frame_index] == 10
        logging.debug(f"Frame {frame_index + 1} is Strike: {result}")
        return result

    def _is_spare(self, frame_index):
        """ 
        Checks if the rolls at both frame_index and frame_index + 1 form a spare (if the total number of pins knocked down is equal to 10, it is a spare).
        
        Args: 
            frame_index (int): The index of the first roll in the frame.
        
        Returns:
            bool: True if the rolls form a spare (pins knocked down equals 10), else False.
        """
        result = frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        logging.debug(f"Frame {frame_index + 1} is Spare: {result}")
        return result

    def _strike_bonus(self, frame_index):
        """ 
        Calculates the bonus for a strike, which is the total pins knocked down in the next two rolls.
        
        Args:
            frame_index (int): The index of the strike roll.
        
        Returns:
            int: The bonus value for the strike.
        """
        bonus = 0
        if frame_index + 1 < len(self.rolls):
            bonus += self.rolls[frame_index + 1]
        if frame_index + 2 < len(self.rolls):
            bonus += self.rolls[frame_index + 2]

        logging.debug(f"Strike bonus for frame {frame_index + 1}: {bonus}")
        return bonus

    def _spare_bonus(self, frame_index):
        """ 
        Calculates the bonus for a spare, which is the total pins that are knocked down in the next roll.
        
        Args:
            frame_index (int): The index of the first roll in the spare.
        
        Returns:
            int: The bonus value for the spare.
        """
        bonus = self.rolls[frame_index + 2]
        logging.debug(f"Spare bonus for frame {frame_index + 1}: {bonus}")
        return bonus
