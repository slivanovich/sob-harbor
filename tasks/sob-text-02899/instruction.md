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
Spectrum (song): "Spectrum" is a song by Russian-German electronic music producer Zedd.  It features the vocals from American singer Matthew Koma.  It was released as a single on June 4, 2012, and serves as the first single from Zedd's debut studio album "Clarity".  It was written by Koma and Zedd.

F1 2011 (video game): F1 2011 is a video game created by Codemasters based on the 2011 Formula One season.  It is the sequel to the 2010 video game based on the same series.  The game was released in September 2011 on the Microsoft Windows, PlayStation 3 and Xbox 360 platforms, November 2011 on the Nintendo 3DS and February 2012 on the PlayStation Vita.  It has sold 3.5 million units worldwide.  The game engine is based on the new EGO 2.0 engine, an unofficially titled evolution of the EGO 1.5 engine that was created specially for the title.

F1 2016 (video game): F1 2016 is a racing game which is based on the 2016 Formula One season and was developed by Codemasters Birmingham, published by Codemasters, distributed by Square Enix in North America and Ubisoft in Japan.  The game is the eighth instalment in the "F1" franchise developed by Codemasters.  The game was released on 19 August 2016 on PlayStation 4, Xbox One and PC.  The game was also released for iOS, Android and tvOS on November 10, 2016.  A Mac version by Feral Interactive was released on April 7, 2017.

Clarity (Zedd song): "Clarity" is a song by Russian-German electronic dance music producer Zedd featuring the vocals of British singer Foxes.  It serves as the third single from his debut studio album of the same name.  The song was written by Zedd, Matthew Koma, Porter Robinson and Skylar Grey and released as iTunes Single of the Week on October 2, 2012, and as an EP on February 12, 2013 by Interscope Records.  Zedd has released an extended mix of the song exclusively on Beatport on November 12, 2012.

F1 2012 (video game): F1 2012 is a video game developed by Codemasters.  It is based on the 2012 Formula One season, and is the sequel to "F1 2010" and "F1 2011".  It is the fourth Formula One game developed by the Codemasters studios after the company renewed its licence to develop the official games of the series.  It was announced on 18 March 2012, co-inciding with the first race of the 2012 season.  The game was released in September 2012.  It uses the EGO Engine.

F1 2017 (video game): F1 2017 is a racing video game developed and published by Codemasters.  It was released for PlayStation 4, Xbox One, macOS and Windows on 25 August 2017.  The game is based on the 2017 Formula One season and includes all of the twenty circuits, twenty drivers and ten teams competing in the season.  "F1 2017" is the ninth installment in the "Formula One" video games franchise developed by Codemasters.  The macOS version, developed by Feral Interactive, was released simultaneously with the other versions - a first in the series' history.

F1 2015 (video game): F1 2015 is a racing game based on the 2015 Formula One season developed by Codemasters.  It is the seventh Formula One game produced by the same studio.  It was released on July 10, 2015, and features the team and driver line-ups from the 2015 season, including the Autódromo Hermanos Rodríguez.  It also features all the drivers, cars and circuits from the 2014 season (i.e. Caterham F1, and the Hockenheimring, which was removed from the calendar).  It is the first title developed by Codemasters for the eighth generation consoles.

F1 2013 (video game): F1 2013 is a video game developed by Codemasters based on the 2013 Formula One season.  It is the fifth Formula One game developed by the Codemasters studios after the company renewed its license to develop the official games of the series.  It uses the EGO Engine.  A notable credit is the opening video features the song "Clarity" by Zedd featuring Foxes.

F1 Race Stars: F1 Race Stars is a video game developed by Codemasters, released in November 2012.  It is a kart racing game loosely based on the 2012 Formula One season, with circuits redesigned to feature loops, jumps and short-cuts.  It is a spin-off from the traditional "Formula One" video games, and is the first kart-racing game developed by Codemasters.  The player is able to choose cartoonish versions of Formula One racing drivers, such as Sebastian Vettel, Lewis Hamilton, Kimi Räikkönen, Nico Rosberg, Mark Webber, Michael Schumacher and Fernando Alonso.  It was announced on 13 July 2012 at the San Diego Comic-Con International.  Codemasters have described the game as being designed to emphasise entertainment rather than simulation.  On 6 December 2012 it was confirmed to be ported to Wii U under the title F1 Race Stars: Powered Up Edition, where it was released on 16 January 2014.

Stay the Night (Zedd song): "Stay the Night" is a song by Russian-German electronic dance music producer Zedd, from the deluxe edition (2013) of his debut studio album, "Clarity " (2012).  It features vocals from Hayley Williams, the lead singer of American rock group Paramore.  The song was written by Zedd, Williams, Benjamin Eli Hanna, and Carah Faye.  "Stay the Night" was released to digital retailers on September 10, 2013, by Interscope Records as the lead single off the deluxe edition of "Clarity", and the fourth overall single from the album.

Question: F1 2013 is a video game developed by Codemasters based on the 2013 Formula One season, a notable credit is the opening video features "Clarity" is a song by which Russian-German electronic dance music producer featuring the vocals of British singer Foxes?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "producer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the music producer."
        },
        "nationality": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The nationality or nationalities of the producer."
        },
        "music_genre": {
          "type": "string",
          "description": "The genre of music produced."
        }
      },
      "required": [
        "name",
        "nationality",
        "music_genre"
      ],
      "additionalProperties": false
    },
    "featured_vocalist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the featured vocalist."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the featured vocalist."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "video_game_featuring_song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the video game that features the song."
        },
        "feature_context": {
          "type": "string",
          "description": "The specific context in which the song is featured in the game."
        }
      },
      "required": [
        "title",
        "feature_context"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the Russian-German electronic dance music producer."
    }
  },
  "required": [
    "song_title",
    "producer",
    "featured_vocalist",
    "video_game_featuring_song",
    "final_answer"
  ],
  "additionalProperties": false
}
