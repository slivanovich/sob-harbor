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
FC Brunsviga 1896 Braunschweig: FC Brunsviga Braunschweig was a German association football club from the city of Braunschweig, Lower Saxony.  The short-lived club was founded in 1896 by students of the local teacher's college and was disbanded sometime in 1901.  It is notable as one of the founding members of the German Football Association (Deutscher Fußball Bund or German Football Association) at Leipzig on 28 January 1900.

SpVgg Leipzig: SpVgg Leipzig is a German association football club from the city of Leipzig, Saxony.  It was formed on 15 February 1899 as the football department of gymnastics club "ATV Leipzig-Lindenau" and became independent as "Spielvereinigung Leipzig" in 1903.  Alongside "VfB Leipzig" and "Dresdner SC", "SpVgg" was one of the most successful pre-war sides in Saxony.

Sportbrüder Leipzig: Sportbrüder Leipzig was a German association football club from the city of Leipzig, Saxony.

Anthony Jung: Anthony Jung (born 3 November 1991) is a German footballer who currently plays for Brøndby on loan from RB Leipzig.

RB Leipzig: RasenBallsport Leipzig e.V., commonly known as RB Leipzig, is a German association football club based in Leipzig, Saxony.  The club was founded in 2009 by initiative of energy drink-maker Red Bull GmbH who purchased a playing right of the fifth division side SSV Markranstädt with the intention of advancing the new club to the top-flight Bundesliga within eight years.  Men's professional football is run by the spin-off organization "RasenballSport Leipzig GmbH".  RB Leipzig plays its home matches at the Red Bull Arena.

Vorwärts Leipzig: ASG Vorwärts Leipzig was a German association football club from the city of Leipzig, Saxony.  The history of the club is marked by several wholesale transfers of the player squad to other cities.  The team was founded in 1951 as "Sportsverein Volkspolizei Vorwärts Leipzig" as the sports club of the Volkspolizei (English: People's Police, the East German national police) based in the city.  The name Vorwärts was used in East Germany by those clubs associated with the armed forces, paramilitary organizations, and police.

Wacker Leipzig: SC Wacker Leipzig was a German association football club playing in Leipzig, Saxony.  The club was formed 24 February 1895 out of the merger of the school clubs "Concordia Leipzig" and "Saxonia Leipzig".  "Wacker" was a founding member of the German Football Association (Deutscher Fussball Bund) in 1900.

Olympia Leipzig: SG Olympia Leipzig is a German association football club based in Leipzig, Saxony.

TuRa Leipzig: TuRa Leipzig was a German association football club active before World War II from the city of Leipzig, Saxony.  Successor sides included "BSG Chemie Leipzig", which was part of East German football competition, and "FC Sachsen Leipzig", which emerged following German reunification in 1990.

Inter Leipzig: Inter Leipzig is a German association football club located in Leipzig, Saxony.  Their first team competes in the NOFV-Oberliga, the fifth tier of German football.

Question: Anthony Jung currently plays for Brondby on loan from what German association football club that is based in Leipzig, Saxony?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the footballer."
    },
    "current_loan_club": {
      "type": "string",
      "description": "The club the player is currently on loan to."
    },
    "parent_club_info": {
      "type": "object",
      "properties": {
        "club_name": {
          "type": "string",
          "description": "The name of the parent club from which the player is on loan."
        },
        "city": {
          "type": "string",
          "description": "The city where the parent club is based."
        },
        "state": {
          "type": "string",
          "description": "The state or region where the parent club is based."
        },
        "country": {
          "type": "string",
          "description": "The country of the parent club."
        },
        "club_type": {
          "type": "string",
          "description": "The type of the club, e.g., 'association football club'."
        }
      },
      "required": [
        "club_name",
        "city",
        "state",
        "country",
        "club_type"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "current_loan_club",
    "parent_club_info"
  ],
  "additionalProperties": false
}
