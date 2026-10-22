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
David Usher: David Usher (born April 24, 1966) is an English-born Canadian musician, best-selling author, keynote speaker and activist, known as the lead singer of the alternative rock band Moist.

Let It Play: Let It Play is the ninth studio album by Canadian solo artist David Usher.  It was released on October 21, 2016 via David Usher's own music label, Evil Empire Inc..  The album features English translations of French Canadian songs.

Billy Bang: Billy Bang (September 20, 1947 – April 11, 2011), born William Vincent Walker, was an American free jazz violinist and composer.

Brian Robertson (trombonist): Brian Robertson (born October 19, 1979) is the trombone player for the Orange County-based third-wave ska band Suburban Legends and, along with Vincent Walker, is one of the two members to have played with the band since its origin as Bomb Squad.  He met other ex-Suburban Legends / Bomb Squad members, trumpet player Aaron Bertram and best friend and trombone player Ryan Dallas Cook through the Huntington Beach High School Marching Band.  In 2007, Robertson started to be known by the nickname 'Robot', most likely a reference to the dance moves he does onstage with the band, the first three letters of his last name, and/or to avoid confusion with the band's other Brian, Brian Klemm.

Vincent Walker: Vincent Francis Walker (born March 2, 1980), better known as Vince Walker, is an American multi-instrumentalist, best known as the lead singer of third-wave ska band Suburban Legends.  He was formerly the lead trumpet player, and left sometime after the release of "Rump Shaker", but returned to the band in September 2005 for the band's appearance on the Jerry Lewis MDA Telethon, which happened to be lead singer Tim Maurer's last performance.  He replaced Maurer as the singer in an odd switching of roles, and continues with the band as frontman.

Vince Foster: Vincent Walker "Vince" Foster Jr. (January 15, 1945 – July 20, 1993) was a Deputy White House Counsel during the first half-year of President Bill Clinton's administration.  Prior to that, he was a partner at Rose Law Firm in Little Rock, Arkansas, where he was a colleague and friend of Hillary Rodham Clinton and where, as "The Washington Post" later wrote, he rose to "the pinnacle of the Arkansas legal establishment."  At the White House he was unhappy with work in politics and spiraled into depression.  His death by gunshot was attributed by five official or governmental investigations to suicide but several conspiracy theories emerged.

Black Black Heart: "Black Black Heart" is a song written by David Usher and Jeff Pearce and released as a second single off Usher's 2001 album "Morning Orbit".

Day Job (Suburban Legends album): Day Job is Suburban Legends' fifth album, released on April 3, 2012.  Aaron Bertram, Brian Robertson, Derek Rock, and Vincent Walker appeared on local online radio program "TNN Radio" to announce the album on February 18, 2012.

Charles Vincent Walker: Charles Vincent Walker FRS (20 March 1812 – 24 December 1882) was an English electrical engineer and publisher, a major influence on the development of railway telecommunications, he was also the first person to send a submarine telegraph signal.

Tim Maurer: Timothy Robert "Tim" Maurer (born October 10, 1980) is an American singer, best known as the former lead singer of third-wave ska band Suburban Legends.  He has left the band on two separate occasions.  The first was in 2000 after the recording of Origin Edition.  He rejoined the band in early 2002 after his replacement singer Chris Batstone left the band.  He officially left the band again in September 2005 after the band's third consecutive appearance on the Jerry Lewis MDA Telethon, performing a new song entitled "Moving Closer."  The band's former trumpet player, Vincent Walker, rejoined the band for the performance, then took over as lead singer afterward.  Maurer returned for a final performance with the band on November 29, 2005 at Huntington Beach High School for a benefit show for the Ryan Dallas Cook Memorial Fund, which was set up following the death of Suburban Legends' trombonist Dallas Cook.

Question: Who is older, Vincent Walker or David Usher?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_a": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first person being compared."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the first person in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "person_b": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second person being compared."
        },
        "birth_date": {
          "type": "string",
          "format": "date",
          "description": "The birth date of the second person in YYYY-MM-DD format."
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "older_person_name": {
      "type": "string",
      "description": "The name of the person who is older."
    },
    "older_person_birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the older person in YYYY-MM-DD format."
    },
    "comparison_statement": {
      "type": "string",
      "description": "A statement summarizing the age comparison."
    }
  },
  "required": [
    "person_a",
    "person_b",
    "older_person_name",
    "older_person_birth_date",
    "comparison_statement"
  ],
  "additionalProperties": false
}
