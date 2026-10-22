Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Mahboob Chowk Clock Tower: Mahboob Chowk Clock Tower is a five-storied architectural clock tower which was built in 1892 by Asman Jah, Prime Minister of Hyderabad.  The Mahbood Chowk area is considered to be an important part of Hyderabad architectural heritage.  The clock tower is erected in the midst of the small garden; it has four large clocks on its sides which enable the time to be seen from any direction.  The clock tower is designed is in the Turkish style.  The tower is located west of the Charminar, not far from Laad Bazaar.

Piliyandala Clock Tower: The Piliyandala Clock Tower is located in the Piliyandala, Sri Lanka.  The clock tower is a popular landmark of the Piliyandala.  According to local residents and documentation, this clock tower is one of the tallest on the island rising to a height of 23.8 m with a 4.9 m girth.  The clock tower in existence for more than sixty years, is considered to be of archaeological value, thus providing the Piliyandala town with a historical background.

Nusretiye Clock Tower: Nusretiye Clock Tower, aka Tophane Clock Tower, is a clock tower situated in Tophane, a neighborhood in Beyoğlu district of Istanbul, Turkey next to Nusretiye Mosque and Tophane Kiosk at the European waterfront of Bosphorus.  It was ordered by the Ottoman sultan Abdülmecid I (1823-1861), designed by architect Garabet Amira Balyan and completed in 1848.

Galle Clock Tower: The Galle Clock Tower (or Anthonisz Memorial Clock Tower) is located within the Galle Fort in Galle, Sri Lanka.  The Clock Tower is a popular landmark and overlooks the central Moon Bastion, on the site of the former guard room.  The Clock Tower was constructed in 1883, paid for through public subscriptions by the people of Galle, in recognition of Dr. P. D. Anthonisz.  The clock itself was the sole gift of a grateful patient, Mudaliyar Samson de Abrew Rajapakse.

Clock Tower of Murshidabad: The Clock Tower of Murshidabad (locally known just as "Clock Tower" or "Ghari Ghar", also known as "Big Ben of Murshidabad") is a clock tower in the Nizamat Fort Campus in West Bengal, India.  The clock tower stands in the garden space between the Nizamat Imambara and the Hazarduari Palace; to its east, hardly a few feet away, is the old Madina Mosque and the Bacchawali Tope.

Birgu Clock Tower: The Birgu Clock Tower (Maltese: "It-Torri tal-Arloġġ tal-Birgu" ), also called the "Vittoriosa Clock Tower" and originally the Civic Clock Tower, was a clock tower in Birgu, Malta.  It was located in Victory Square, the city's main square, and it was a prominent landmark in Birgu and the rest of the Three Cities.  The tower was probably built in the Middle Ages, although some sources state that it was constructed in 1549.  It served as a watchtower since it had views over the Grand Harbour and the surrounding countryside, and it saw use during the Great Siege of Malta in 1565.  A clock was installed in the tower in the 17th century.

Clock Tower (series): Clock Tower is a survival horror point-and-click adventure video game series created by Hifumi Kono.  The series includes four games in total.  The first entry, "Clock Tower" (1995), was developed by Human Entertainment and released on the Super Famicom exclusively in Japan.  Human Entertainment developed two more entries, "Clock Tower" (1996) and "" (1998), which were released on the PlayStation and localized outside Japan.  The fourth and most recent title, "Clock Tower 3" (2002), was co-developed by Sunsoft and Capcom for the PlayStation 2.  Gameplay in the series generally involves the player hiding and escaping from enemy pursuers without any weapons to defeat them.  Scissorman is a reoccurring antagonist and sometimes the sole enemy in the game.

Clock Tower (1996 video game): Clock Tower, released in Japan as Clock Tower 2, is a survival horror point-and-click adventure game developed by Human Entertainment and released for the PlayStation in 1996.  It is the second game in the "Clock Tower" series after the original "Clock Tower", which was released exclusively in Japan for the Super Famicom one year prior.  The story takes place in Norway and follows a variety of characters as they attempt to survive the return of Scissorman and uncover the mystery of his seemingly immortal state.  The scenarios encountered and endings vary widely based upon the player's actions.

Dolmabahçe Clock Tower: Dolmabahçe Clock Tower (Turkish: "Dolmabahçe Saat Kulesi" ) is a clock tower situated outside Dolmabahçe Palace in Istanbul, Turkey.  The tower was ordered by Ottoman sultan Abdülhamid II (1842–1918) and designed by the court architect Sarkis Balyan between 1890 and 1895.

Clock Tower, Brighton: The Clock Tower (sometimes called the Jubilee Clock Tower) is a free-standing clock tower in the centre of Brighton, part of the English city of Brighton and Hove.  Built in 1888 in commemoration of Queen Victoria's Golden Jubilee, the distinctive structure included innovative structural features and became a landmark in the popular and fashionable seaside resort.  The city's residents "retain a nostalgic affection" for it, even though opinion is sharply divided as to the tower's architectural merit.  English Heritage has listed the clock tower at Grade II for its architectural and historical importance.

Question: Which of these structures is older, Nusretiye Clock Tower or Dolmabahçe Clock Tower?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_subject_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first clock tower being compared."
        },
        "completion_year": {
          "type": "integer",
          "description": "The year the first clock tower was completed."
        }
      },
      "required": [
        "name",
        "completion_year"
      ],
      "additionalProperties": false
    },
    "comparison_subject_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second clock tower being compared."
        },
        "completion_year": {
          "type": "integer",
          "description": "The year the second clock tower was completed."
        }
      },
      "required": [
        "name",
        "completion_year"
      ],
      "additionalProperties": false
    },
    "older_structure_name": {
      "type": "string",
      "description": "The name of the clock tower that is older."
    },
    "age_difference_years": {
      "type": "integer",
      "description": "The difference in years between the completion of the two structures."
    }
  },
  "required": [
    "comparison_subject_1",
    "comparison_subject_2",
    "older_structure_name",
    "age_difference_years"
  ],
  "additionalProperties": false
}
