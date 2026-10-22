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
Sports Illustrated for Women: Sports Illustrated Women (previously called Sports Illustrated for Women) and also known as SI Women, was a bimonthly sports magazine covering (according to its statement of purpose) "the sports that women play and what they want to follow, from basketball to tennis, soccer to volleyball, field hockey to ice hockey and figure skating and more.  It featured real athletes, told their real stories and gave the real scoop on women's sports.  "Sports Illustrated for Women" was published by Time Inc." It ran for 20 issues, between March 2000 and November 2002, targeting an audience of women, 18–34 years old, with "a passion for sports."

Lorin Thompson: Lorin Thompson, Lorin Hartwell Jr Thompson, (1911–1997), was a muralist, artist, and creator and illustrator of the character "Ranger Rick" for the National Wildlife Federation's children's magazine, Ranger Rick.

André Laguerre: Marc André Laguerre (February 21, 1915 – January 18, 1979) was a journalist and magazine editor, best known as the managing editor of "Sports Illustrated" from 1960 to 1974, during which time he oversaw the growth in the magazine from a niche publication to become the industry leader in weekly sports magazines.  It was under his leadership that the annual "Sports Illustrated Swimsuit Issue" was first published.  When he retired in 1974, he had been managing editor of the magazine for 704 issues, then a record among magazines published by Time, Inc., SI's parent company.

Sports Illustrated: Sports Illustrated is an American sports media franchise owned by Time Inc. Its self-titled magazine has over 3 million subscribers and is read by 23 million people each week, including over 18 million men.  It was the first magazine with circulation over one million to win the National Magazine Award for General Excellence twice.  Its swimsuit issue, which has been published since 1964, is now an annual publishing event that generates its own television shows, videos and calendars.

Ranger Rick: Ranger Rick, originally Ranger Rick's Nature Magazine, is a children’s nature magazine that is published by the United States National Wildlife Federation.  The magazine offers feature articles and activities for children, ages 7 and up, in order to spark their interest in the outdoors and become more actively involved in the environment.  The magazine's primary intention is to instill a passion for nature and promote activity outdoors.  NWF also publishes two companion magazines, "Ranger Rick Jr.", which is aimed at ages 4–7, and "Ranger Rick Cub", which is aimed at kids 0–4 years old.)

Larry Johnson (author): Larry Johnson (born in Albuquerque, New Mexico) is an American author and former employee of the Alcor Life Extension Foundation (Alcor), a cryonics company for whom he once served as chief operating officer.  He received notoriety with the release of the August 13, 2003 issue of "Sports Illustrated".  "Sports Illustrated" sportswriter Tom Verducci, along with Johnson's input, published an article about “What Really Happened to Ted Williams?"  Immediately following the "Sports Illustrated" article, Johnson agreed to an interview with Diane Sawyer of Good Morning America.

Inside Sports: Inside Sports magazine was a major general interest sports magazine in the United States.  Launched in 1979 by Newsweek, it was designed as an edgier, monthly alternative to the longer-running "Sports Illustrated" and "SPORT Magazine" brands.  In addition to 12 issues a year, it featured a "Swimsuit Spectacular" ("IS"' answer to the famous Sports Illustrated Swimsuit Issue).

University of South Carolina steroid scandal: In October 1988, "Sports Illustrated" published a lengthy article on alleged steroid abuse in the football program at the University of South Carolina.  The article, titled "The Nightmare of Steroids" and written by University of South Carolina football player Tommy Chaikin in collaboration with "Sports Illustrated"<nowiki>'</nowiki>s Rick Telander, alleged the widespread use of steroids in the football program at the school.  Following the article, a federal grand jury indicted four University of South Carolina football coaches in connection with steroid distribution to players.  Three of the coaches pleaded guilty in plea-bargain arrangements and the fourth was acquitted.  The episode was listed among "some of college football's biggest scandals" by sports reporter Tom Weir of USA Today.

Heinz Kluetmeier: Heinz Kluetmeier (born 1942) is a German-born American sports photographer for "Sports Illustrated".  He has covered every Olympic Games for the magazine since the 1972 Munich games except one, and has over 100 "Sports Illustrated" cover photographs to his credits.  He has served two stints as the magazine's director of photography and received the Lucie Award for outstanding achievement in sports photography in October 2007.

Sports Illustrated Kids: Sports Illustrated Kids (SI Kids, trademarked Sports Illustrated KIDS, sometimes Sports Illustrated for Kids) is a monthly spin-off of the weekly U.S. sports magazine "Sports Illustrated".  "SI Kids" was launched in January 1989 and includes sports coverage with less vocabulary and emphasis on humor.  The magazine's secondary purpose is to market sports to children.

Question: Which magazine series has the primary intention to instill a passion for nature and involvement in the environment, Sports Illustrated or Ranger Rick?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_series_name": {
      "type": "string",
      "description": "The name of the magazine series that matches the specified primary intention."
    },
    "primary_intention": {
      "type": "string",
      "description": "The stated primary intention of the identified magazine series."
    },
    "comparison_magazines": {
      "type": "array",
      "description": "Details of the magazines considered in the comparison.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the magazine series."
          },
          "stated_purpose": {
            "type": "string",
            "description": "The stated purpose or focus of the magazine series."
          }
        },
        "required": [
          "name",
          "stated_purpose"
        ],
        "additionalProperties": false
      }
    },
    "matches_criteria": {
      "type": "boolean",
      "description": "Indicates whether the identified magazine series' intention matches the criteria in the question."
    }
  },
  "required": [
    "magazine_series_name",
    "primary_intention",
    "comparison_magazines",
    "matches_criteria"
  ],
  "additionalProperties": false
}
