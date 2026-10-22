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
Franco, Ciccio e il pirata Barbanera: Franco, Ciccio e il pirata Barbanera ("Franco, Ciccio and Blackbeard the Pirate") is a 1969 Italian comedy film directed by Mario Amendola.

Along Came Jones (film): Along Came Jones is a 1945 Western comedy film starring Gary Cooper, Loretta Young, William Demarest, and Dan Duryea, in which Cooper mercilessly spoofs his own slow-talking cowboy persona.  The movie was adapted by Nunnally Johnson from the novel "Useless Cowboy" by Alan Le May, and directed by Stuart Heisler.

The Castaway Cowboy: The Castaway Cowboy is a 1974 American adventure film released by Walt Disney Productions starring James Garner, Vera Miles, Eric Shea, and Robert Culp about a Texas rancher who gets shanghaied, then jumps ship and finds himself washed ashore in Hawaii.  Filmed on location in Hawaii, the movie was directed by Vincent McEveety and written by Don Tait and Richard M. Bluel.

Ghost Day (film): Ghost Day (Thai: แก๊งค์ตบผี ) is a 2012 Thai horror comedy film directed by Thanit Jitnukul, Titipong Chaisat, and Sorathep Vetwongsatip.  The film is set in modern-day Bangkok where the production team behind the television series "Ghost Day" is told by their show is going to be cancelled.  To stop the end of their program, the staff decide to find a real haunted area and, after viewing an video online by ghostbusters Mhen (Apisit Opasaimlikit) and Chiad (Padong Songsang), they decide to approach them to do a deal.  Mhen and Chiad have brought along a real female ghost who appears and possesses the show's director, Pom (Boriboon Chanruang).

Blackbeard's Ghost: Blackbeard's Ghost is a 1968 American fantasy comedy film produced by Walt Disney Productions, starring Peter Ustinov, Dean Jones, Suzanne Pleshette and directed by Robert Stevenson.  It is based upon the novel of the same name by Ben Stahl and was shot at the Walt Disney Studios.  The Disney Channel aired this film until the late 1990s .

Castaway on the Moon: Castaway on the Moon (; lit.  "Mr Kim's drifting experience": 표류: drifting; hanja: 漂流記) is a 2009 South Korean romantic comedy film written and directed by Lee Hae-jun.  It is a love story between a suicidal man turned castaway on Bamseom in the Han River and an agoraphobic woman who is addicted to Cyworld.

Road to Morocco: Road to Morocco is a 1942 American comedy film starring Bing Crosby, Bob Hope and Dorothy Lamour, and featuring Anthony Quinn and Dona Drake.  The film, which was written by Frank Butler and Don Hartman and directed by David Butler for Paramount Pictures, is the third of the ""Road to …"" films.  It was preceded by "Road to Zanzibar" (1941) and followed by "Road to Utopia" (1946).  The story is about two fast-talking guys castaway on a desert shore and sold into slavery to a beautiful princess.  The setting is in Morocco during Spanish Rule.

The Cowboy and the Lady (1938 film): The Cowboy and the Lady is a 1938 American western romantic comedy film directed by H.C. Potter, and starring Gary Cooper and Merle Oberon.  Written by S.N. Behrman and Sonya Levien, based on a story by Frank R. Adams and veteran film director Leo McCarey, the film is about a beautiful socialite masquerading as a maid who becomes involved with an unpretentious, plain-spoken cowboy who is unaware of her true identity.  "The Cowboy and the Lady" won an Academy Award for Sound Recording (Thomas Moulton), and was nominated for Original Score (Alfred Newman) and Original Song ("The Cowboy and the Lady" by Lionel Newman and Arthur Quenzer).

Irumbukkottai Murattu Singam: Irumbukkottai Murattu Singam (English: "The Iron Fort's Furious Lion" ) is a 2010 Indian Tamil western comedy film directed by Chimbu Deven, starring choreographer-turned-actor Lawrence Raghavendra, Sandhya, Lakshmi Rai and Padmapriya in lead roles.  The film is a "Western adventure comedy film" based on Cowboy stories, which is set in the 19th century paying homages to many western films.  The film's shooting commenced in April 2009 and released on 7 May 2010, positive reviews for its story.In Tamil cinema, after the movie Gangaa, this is a full length cowboy movie being taken after 38 years.  The movie was appreciated to be in the standards of an original Italian cowboy movies.  The film comically highlights the current world politics.

Lt. Robin Crusoe, U.S.N.: Lt. Robin Crusoe USN is a 1966 comedy film released and scripted by Walt Disney, and starring Dick Van Dyke as a U.S. Navy pilot who becomes a castaway on a tropical island.  Some filming took place in San Diego, while a majority of the film was shot on Kauai, Hawaii.

Question: Which was a comedy film,  Blackbeard's Ghost or The Castaway Cowboy?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_comparison": {
      "type": "object",
      "properties": {
        "film_1_title": {
          "type": "string",
          "description": "The title of the first film being compared."
        },
        "film_1_is_comedy": {
          "type": "boolean",
          "description": "True if the first film is a comedy, false otherwise."
        },
        "film_2_title": {
          "type": "string",
          "description": "The title of the second film being compared."
        },
        "film_2_is_comedy": {
          "type": "boolean",
          "description": "True if the second film is a comedy, false otherwise."
        }
      },
      "required": [
        "film_1_title",
        "film_1_is_comedy",
        "film_2_title",
        "film_2_is_comedy"
      ],
      "additionalProperties": false
    },
    "comedy_film_identified": {
      "type": "string",
      "description": "The title of the film identified as a comedy."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why the identified film is a comedy and the other is not."
    }
  },
  "required": [
    "film_comparison",
    "comedy_film_identified",
    "reasoning"
  ],
  "additionalProperties": false
}
