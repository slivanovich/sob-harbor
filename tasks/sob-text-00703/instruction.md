{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSpencer Garrett: Spencer Garrett (born Spencer Garrett Heckenkamp; September 19, 1963) is an American actor who has appeared in television programs, television films, films, and in minor roles in blockbuster productions like \"\", \"Public Enemies\", and \"Air Force One\".\n\nBilly Crudup: William Gaither Crudup ( ; born July 8, 1968) is an American actor.  He is known for supporting roles in films including \"Almost Famous\", \"Big Fish\", \"\", \"Watchmen\", \"Public Enemies\", \"Spotlight\" and \"\", as well as lead roles in films including \"Without Limits\", \"Jesus' Son\", \"Dedication\" and the animated film \"Princess Mononoke\".  He is due to appear in the upcoming 2017 superhero film \"Justice League\" as Doctor Henry Allen.\n\nThe New Batman/Superman Adventures: The New Batman/Superman Adventures is a name given to a package series that combined \"\" with \"\" and \"The New Batman Adventures\" produced by Warner Bros.  Animation.  It aired from 1997–2000 on Kids' WB.  Each half-hour episode in the hour-and-one-half block featured either a single repeat from the original \"Superman: The Animated Series\" run, the original \"Batman: The Animated Series\" run, or a brand new story featuring Batman made specifically for this series, drawn in an animation style to match \"Superman: The Animated Series\".  These new stories focus more on Batman's supporting cast and introduced new characters such as Tim Drake.  The two animated universes were united in the \"Superman\" episode \"World's Finest\", which tells the story of Batman and Superman's first meeting.  The new Batman episodes that began airing in the Fall 1997 season were later released as a DVD box set of \"Batman: The Animated Series\" as Volume 4.  New Superman episodes that later aired in the Fall 1998 season and onward are now considered to be the third season of \"Superman: The Animated Series\".\n\nWorld's Finest (film): World's Finest is a fan film directed by Sandy Collora.  It works as a trailer to a movie that does not exist: the long-awaited cinematic team-up of Superman and Batman.  While Superman and Batman had appeared together often in comic books and in animation (notably \"Super Friends\"), there would not be an official live-action pairing until \"\", which was released twelve years later.  The title refers to a famous comic series that featured Batman and Superman working together in every issue.\n\nSuperman/Batman: Public Enemies: Superman/Batman: Public Enemies is a 2009 original direct-to-video animated superhero film adaptation of \"Public Enemies\"—the opening story arc of DC Comics' \"Superman/Batman\"—which focuses on Superman and Batman teaming up to prevent a meteorite from striking Earth and take down Lex Luthor, who has been elected President of the United States.  The film is the sixth in the line of the DC Universe Animated Original Movies line released by Warner Premiere and Warner Bros.  Animation.  Voice actors from the DCAU reprised their roles, although it is not a DCAU production and is said not to be connected with that universe beyond sharing of voice actors.  The film is directed by Sam Liu.\n\nRa's al Ghul: Ra's al Ghul (Arabic: رأس الغول‎ ‎ \"Raʾs al-Ġūl\"; \"Ghoul's Head\" or \"Demon's Head\") is a fictional supervillain appearing in American comic books published by DC Comics, commonly as an adversary of the superhero Batman.  Created by editor Julius Schwartz, writer Dennis O'Neil and artist Neal Adams, the character first appeared in \"Batman\" #232's \"Daughter of the Demon\" (June 1971).  The character is one of Batman's most enduring enemies and belongs to the collective of adversaries that make up Batman's rogues gallery, though given his high status as a supervillain, he has also come into conflict with Superman and other superheroes in the DC Universe.\n\nPublic Enemiez: Public Enemiez is the eleventh studio album by rapper Daz Dillinger.  A release date for the album was planned for mid July 2009 to coincide with the release of the upcoming film Public Enemies of which the album is named after.  The album ended up being released on August 11, 2009.\n\nHero of the Rails: Hero of the Rails is a 2009 CGI adventure drama special and film spin-off of the TV series \"Thomas & Friends\".  The film introduces full CGI animation, replacing model work and the addition of a voice cast for the characters alongside the narration to the TV series.  The film features the voice of Ben Small and Martin Sherman as Thomas the Tank Engine for the UK and US respectively.  It was first released on DVD and to iTunes on 12 January 2010.  To promote the film a \"Day Out With Thomas 2010: The Hero of the Rails Tour\" was held at locations such as the Illinois Railway Museum, where guests could participate in activities such as arts and crafts or ride on a 15-ton replica of Thomas the Tank Engine.  A mobile app, \"Thomas & Friends: Hero of the Rail\", was released in May 2011.\n\nSuperman/Batman: Apocalypse: Superman/Batman: Apocalypse is a 2010 direct-to-video animated superhero film based on the \"Superman/Batman\" comic storyline \"The Supergirl from Krypton\" and is a sequel to \"\".  The art style is partly based on that of Michael Turner, who penciled the \"Superman/Batman\" comic book arc.  The film is the ninth in the DC Universe Animated Original Movies line released by Warner Premiere and Warner Bros.  Animation and the first sequel in the line.  It was released on September 28, 2010.  The film stars Andre Braugher, Kevin Conroy, Tim Daly and Summer Glau.  Despite the title, the film focuses primarily on the introduction of Supergirl and her relationship with Superman.  Batman plays a supporting role.\n\nPublic Enemies (2009 film): Public Enemies is a 2009 American biographical mob drama film directed by Michael Mann and written by Mann, Ronan Bennett and Ann Biderman.  It is an adaptation of Bryan Burrough's non-fiction book \"Public Enemies: America's Greatest Crime Wave and the Birth of the FBI, 1933–34\".  Set during the Great Depression, the film chronicles the final years of the notorious bank robber John Dillinger (Johnny Depp) as he is pursued by FBI agent Melvin Purvis (Christian Bale), Dillinger's relationship with Billie Frechette (Marion Cotillard), as well as Purvis' pursuit of Dillinger's associates and fellow criminals Homer Van Meter (Stephen Dorff) and Baby Face Nelson (Stephen Graham).\n\nQuestion: What year were the films Hero of the Rails and Superman/Batman: Public Enemies released?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"films\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"title\": {\n            \"type\": \"string\"\n          },\n          \"release_year\": {\n            \"type\": \"integer\"\n          }\n        },\n        \"required\": [\n          \"title\",\n          \"release_year\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_release_year\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if all listed films share the same release year.\"\n    },\n    \"overall_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The common release year if 'common_release_year' is true.\"\n    }\n  },\n  \"required\": [\n    \"films\",\n    \"common_release_year\",\n    \"overall_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "films": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "release_year": {
              "type": "integer"
            }
          },
          "required": [
            "title",
            "release_year"
          ],
          "additionalProperties": false
        }
      },
      "common_release_year": {
        "type": "boolean",
        "description": "True if all listed films share the same release year."
      },
      "overall_release_year": {
        "type": "integer",
        "description": "The common release year if 'common_release_year' is true."
      }
    },
    "required": [
      "films",
      "common_release_year",
      "overall_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
