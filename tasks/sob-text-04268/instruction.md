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
Holby City (series 1): The first series of the British medical drama television series "Holby City" commenced airing in the United Kingdom on BBC One on 12 January 1999, and concluded on 9 March 1999.  The show was created by Mal Young and Tony McHale as a spin–off from the BBC medical drama "Casualty", intended to follow the treatment of patients from "Casualty" as they were transferred onto the hospital's surgical wards.  McHale served as the programme's lead writer throughout the first series, which ran for nine episodes.  Young cast actors who were already established names in the acting industry, particularly from a soap opera background.  Several cast members shadowed real surgeons and nurses in preparation for their roles to increase the show's realism.  The series received mixed reviews from critics.  It was compared favourably with "Casualty", but received negative reviews in which it was contrasted poorly with the American medical drama "ER".  The series première attracted 10.72 million viewers, falling to 8.51 million by the series finale.

Gonks Go Beat: Gonks Go Beat is a 1965 British science fiction / musical fantasy film, directed by Robert Hartford-Davis.  It stars Kenneth Connor and Frank Thornton.  "Gonks Go Beat" is loosely based on the "Romeo and Juliet" storyline and features 16 musical numbers performed by a variety of artists, including Lulu and the Luvvers, The Nashville Teens and members of the Graham Bond Organisation including Ginger Baker, Jack Bruce and Dick Heckstall-Smith.  Other musical contributors were – and remained – obscure.  The film includes an early appearance by the actor Derek Thompson performing with his twin sister Elaine (credited as Elain).

Richard Winsor: Richard Winsor (born 4 January 1982) is a British actor and dancer.  He is best known for his role as Caleb Knight in the long-running BBC television medical drama series "Casualty" from January 2014 until April 2017, when his character was killed off after being stabbed by a patient's relative.

List of Holby City episodes: "Holby City" is a British medical drama television series that premiered on 12 January 1999 on BBC One.  The series was created by Tony McHale and Mal Young as a spin-off from the established BBC medical drama "Casualty".  It is set in the same hospital as "Casualty", Holby General, in the fictional city of Holby, however "Holby City" is filmed at Elstree Studios in Borehamwood, while "Casualty" is filmed in Cardiff.  Occasional crossovers between the two shows are broadcast as "Casualty@Holby City".  In 2006, "HolbyBlue", a police procedural spin-off from "Holby City", went into production.  Its second season launched with a "Holby City" crossover episode.

Characters of Casualty: "Casualty" is a British medical drama television series that premiered on 6 September 1986 on BBC One.  The series was created by Jeremy Brock and Paul Unwin.  It is set in the fictional Holby City Hospital, in the equally fictitious city of Holby, and features occasional crossovers of characters and plots with spin-off show "Holby City".  "Casualty" follows the professional and personal lives of the doctors, nurses, paramedics, hospital management and patients at Holby General.  It features an ensemble cast of regular characters, and began with 10 main characters in its first series, all but two – Charlie Fairhead (played by Derek Thompson) and Lisa "Duffy" Duffin (played by Cathy Shipton) – have since left the show.  Many main characters have been written in and out of the series since.  In addition, "Casualty" features guest stars each week, as well as recurring guests that take part in story arcs that span a portion of a series or multiple series'.

Exile (Casualty): "Exile" is the thirty-second episode of the twenty-ninth series of the British medical drama "Casualty".  It was written by Kelly Jones, directed by Steve Hughes, and produced by Jonathan Phillips.  "Exile" first aired on 16 May 2015 on BBC One in the United Kingdom.  The plot sees Charlie Fairhead (Derek Thompson) and Connie Beauchamp (Amanda Mealing) travel to Bucharest to help Charlie's son Louis (Gregory Foreman), who has become a heroin addict and is planning on selling his kidney to pay his debts.

Derek Thompson (actor): Derek Thompson (born 4 April 1948) is a Northern Irish actor, most notable for playing Charlie Fairhead in the long-running BBC television medical drama series "Casualty".  Thompson has played the role since the series' inception in 1986.

Gillian Kearney: Gillian Louise Kearney (born 9 May 1972, Liverpool, Merseyside) is an English actress best known for her early role as Debbie McGrath in Channel 4's Liverpool-based soap opera "Brookside" and the spin-off mini-series "Damon and Debbie", and for playing Jessica Harrison in the long-running BBC television medical drama series "Casualty", as well as Emma Barton in the ITV Yorkshire-based soap opera "Emmerdale".

Charlie Fairhead: Charlie Fairhead, played by Derek Thompson, is a fictional character from the BBC British medical drama "Casualty".  He is the longest-serving character having played the role of Charlie for over 30 years and the only remaining original character to have appeared continuously since the first episode on 6 September 1986.  Thompson chose to take a nine-month break from the show in early 2004.  Charlie left the show in series 18 on 17 July 2004 and after five months, returned on 1 January 2005 in series 19.  At the end of series 19, Charlie left again as Thompson returned to his break from the show, with Charlie's exit scenes airing on 20 August 2005.  After four months off-screen, Charlie returned in the series 20 Christmas crossover with "Holby City", which aired on 24 December 2005.  Thompson has remained with the show since, but regularly takes breaks of around two months every year.

Alan David (singer): Alan David is a British singer of the 1960s and 1970s.  He released several singles first for Decca, then for EMI, from 1964 to 1978.  David appeared, playing himself as a singer in a band, in the film "Gonks Go Beat" (1965), and co-hosted the BBC2 TV show "Gadzooks, It's The In Crowd" in June, 1965 with Lulu.

Question: Which actor, most notable for playing Charlie Fairhead in the long-running BBC television medical drama series "Casualty," has an early appearance in Gonks Go Beat?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "notable_role_details": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the character the actor is most notable for playing."
        },
        "series_name": {
          "type": "string",
          "description": "The name of the television series where the notable role appeared."
        },
        "series_type": {
          "type": "string",
          "description": "The genre or type of the television series."
        }
      },
      "required": [
        "character_name",
        "series_name",
        "series_type"
      ],
      "additionalProperties": false
    },
    "film_appearance_details": {
      "type": "object",
      "properties": {
        "film_title": {
          "type": "string",
          "description": "The title of the film in which the actor had an early appearance."
        },
        "appearance_note": {
          "type": "string",
          "description": "A note describing the nature of the appearance in the film."
        }
      },
      "required": [
        "film_title",
        "appearance_note"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "notable_role_details",
    "film_appearance_details"
  ],
  "additionalProperties": false
}
