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
Four Live (New Zealand television programme): Four Live (stylised as FOUR Live) was a New Zealand topical entertainment show that aired weekday afternoons (4.30-6pm) on FOUR.  It was hosted by Drew Neemia and Kanoa Lloyd.  Many guests appeared on the show to feature the latest in music, fashion, entertainment, gaming and film.

The Maxwell Show: The Maxwell Show was a hot talk radio show which aired weekday afternoons on Cleveland rock station WMMS (100.7 FM).  The show began in April 2004, and over the next five years, grew to become the Cleveland radio market's #1 afternoon program in several key demographics.  However, relations between show host Maxwell (Benjamin Bornstein) and WMMS owner Clear Channel steadily grew strained, and in November 2009 the show was cancelled.

Entertainment Desk: Entertainment Desk was a Canadian entertainment news television series, which aired on the Global Television Network in the 1990s.  Anchored by Bob McAdorey, the show aired weekday afternoons.

Commander Tom Show: The Commander Tom Show was a children's television series that aired weekday afternoons on Channel 7 WKBW-TV in Buffalo, New York, premiering on December 20, 1965.

McLean Stevenson: Edgar McLean Stevenson Jr. (November 14, 1927 – February 15, 1996) was an American actor most recognized for his role as Lt. Colonel Henry Blake on the TV series "M*A*S*H".  He was also recognized for his role as Michael Nicholson on "The Doris Day Show".

The Point (radio show): The Point was a Canadian radio program, which aired weekday afternoons on CBC Radio One.  Hosted by Aamer Haleem, the program presented a mix of current affairs and lifestyle interviews and panel discussions.

Terry Meiners: Terry Allen Meiners, born January 22, 1957, is an American radio and television personality on WHAS (AM) and WHAS-TV in Louisville, Kentucky.  On radio, "The Terry Meiners Show" has aired weekday afternoons since 1985, with the show airing 3–7 pm from 1985 to May 15, 2015 and now from 3–6 pm.  Meiners is known for broadcasting impersonations of prominent local citizens, and his satirical interviews of eclectic news figures, comedians, film and television stars, and politicians.  In a region that thrives on college sports, Meiners lampoons the flightiness of University of Louisville (U of L) Cardinals fans and the zealotry of University of Kentucky (UK) Wildcats fans.  Many of Meiners' fabricated callers are dimwitted sports fans delivering a tirade on the air, who then close with the statement "I'll hang up and listen to your answer."

Michael Gibson (TV presenter): Michael Gibson (born 29 October 1980 in Blackburn, Lancashire) is a TV presenter and documentary director.  He presented the "MTV Select" television program which aired weekday afternoons on MTV across Europe.

Game ng Bayan: Game ng Bayan (abbreviated as GNB, lit.  "Game of the Nation") is a short-lived Philippine game show hosted by Robin Padilla and Alex Gonzaga, with Eric Nicolas, Mary Jean Lastimosa and Negi.  It premiered on ABS-CBN and worldwide on The Filipino Channel, replacing "Kapamilya, Deal or No Deal".  It aired weekday afternoons at 5:00-5:45pm (timeslot may vary in some areas nationwide).  This was the fourth localized Kapamilya game show after "Pilipinas, Game KNB? ", "" and "Celebrity Playtime".

America (U.S. TV series): America is an American lifestyle and variety talk show that aired weekday afternoons in syndication during the 1985-86 television season.  The program premiered on September 16, 1985 and was initially hosted by Stuart Damon, Sarah Purcell, McLean Stevenson and Olivia Moens, with Charlie O'Donnell announcing.  "America" was recorded before a live studio audience.

Question: Which American actor most recognized for his role as Lt. Colonel Henry Blake on the TV series "M*A*S*H" was initially a host on an American lifestyle and variety talk show that aired weekday afternoons in syndication during the 1985-86 television season?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the American actor."
    },
    "recognized_role": {
      "type": "string",
      "description": "The specific role the actor is most recognized for."
    },
    "recognized_series": {
      "type": "string",
      "description": "The TV series where the actor played the recognized role."
    },
    "hosted_show_details": {
      "type": "object",
      "properties": {
        "show_name": {
          "type": "string",
          "description": "The name of the American lifestyle and variety talk show."
        },
        "show_type": {
          "type": "string",
          "description": "The genre or type of the hosted show."
        },
        "air_time_description": {
          "type": "string",
          "description": "Description of when the show aired (e.g., weekday afternoons)."
        },
        "air_period": {
          "type": "string",
          "description": "The television season during which the show aired."
        }
      },
      "required": [
        "show_name",
        "show_type",
        "air_time_description",
        "air_period"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "recognized_role",
    "recognized_series",
    "hosted_show_details"
  ],
  "additionalProperties": false
}
