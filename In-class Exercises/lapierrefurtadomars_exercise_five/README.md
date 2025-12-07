# CART 351 – Exercise V: Patterns and MongoDB

## Queries and Visualizations

### Query Three: Positive Mood Entries
- **How the Query Works:** Selects all entries where `after_mood` is positive from the MongoDB collection.
- **Visualization Intention:** `visualizeThree` displays floating “Positive Mood Balloons” to highlight upbeat moods. Colors correspond to different positive moods, and slight upward animation adds a playful, buoyant feeling.

### Query Four: Event Timeline by Mood
- **How the Query Works:** Retrieves all entries sorted by `event_name`.
- **Visualization Intention:** `visualizeFour` shows hovering orbs arranged by event row. Each orb is colored by `after_mood`, and subtle bouncing animation emphasizes differences between moods while keeping the timeline clear.

### Query Five: Monday/Tuesday Event Strength
- **How the Query Works:** Selects entries that occurred on Monday or Tuesday, sorted by `event_affect_strength`.
- **Visualization Intention:** `visualizeFive` presents event strength as floating orbs in a grid. Colors reflect `after_mood`, and gentle floating motion visually conveys the variation in event affect strengths.

### Query Six: Negative Moods by Weather
- **How the Query Works:** Retrieves entries where both `start_mood` and `after_mood` are negative, sorted by `weather`.
- **Visualization Intention:** `visualizeSix` uses static points grouped by weather to clearly show patterns in negative moods. No animation was added to emphasize the structured layout and weather grouping.
