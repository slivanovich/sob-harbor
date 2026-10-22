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
Strychnine in the Soup: "Strychnine in the Soup" is a short story by the British comic writer P. G. Wodehouse.  A part of the Mr. Mulliner series, the story was first published in 1932 in "Strand Magazine".  It also appears in the collections "Mulliner Nights" and "Wodehouse on Crime".  A BBC TV adaptation of the story aired on 9 April 1976 starring John Alderton as Cyril Mulliner and Pauline Collins as Amelia Bassett as part of the Wodehouse Playhouse series of short stories.

Andrew Burt: Andrew Burt (born 23 May 1945 in Wakefield, England) is a retired English actor, who has appeared in many British TV drama series from the 1970s to the present day.  He is perhaps best known as the original Jack Sugden in "Emmerdale Farm", a role he played from 1972 to 1974 (with a brief return in 1976), before handing over the character to another actor, Clive Hornby.  He played the brother of Lesley Whittle in the 1977 film "The Black Panther", and had the eponymous starring role in the BBC series "The Legend of King Arthur" (1979).

John Alderton: John Alderton (born 27 November 1940) is an English actor who is best known for his roles in "Upstairs, Downstairs", "Thomas & Sarah", "Wodehouse Playhouse", "Little Miss" (original TV series), "Please Sir! ", and "Fireman Sam" (The original series).  Alderton has often starred alongside his wife, Pauline Collins.

No, Honestly (song): "No, Honestly" is a song written, performed and produced by Lynsey de Paul, that was the theme for the London Weekend Television comedy series, "No, Honestly", starring Pauline Collins and John Alderton.  The song was the first release on the Jet Records label established by Don Arden. </small> Released on October 18, 1974, it peaked at No. 7 on the UK Singles Chart. </small> The single release was a different version to that used for the TV theme.  In 1975, de Paul received an Ivor Novello Award for Best Theme From a Radio or TV Production. </small>

Thomas Watkins: Thomas David Watkins (c.1876 – ?)  is a fictional character in the ITV drama "Upstairs, Downstairs" and its spin-off "Thomas & Sarah".  He was portrayed by John Alderton.

Laurence Fox: Laurence Paul Fox (born 26 May 1978) is an English actor, singer-songwriter and guitarist, best known for his leading role as DS James Hathaway in the British TV drama series "Lewis" from 2006 to 2015.  His debut album, Holding Patterns, was released in February 2016.

Mulliner's Buck-U-Uppo: "Mulliner's Buck-U-Uppo" is a short story by the British comic writer P. G. Wodehouse.  A part of the Mr. Mulliner series, the story was first published in the United States by Liberty Magazine on September 4, 1926 and in the United Kingdom in The Strand in November 1926, and collected in Meet Mr. Mulliner (1927).  A BBC TV adaptation of the story first aired on 12 December 1978 in the series Wodehouse Playhouse starring John Alderton as Augustine Mulliner and Belinda Carroll as Jane Brandon.

The Last Detective: The Last Detective is a British TV drama series, broadcast on ITV between 7 February 2003 and 31 May 2007, starring Peter Davison as the title character, Detective Constable "Dangerous Davies".  The series is based on the "Dangerous Davies" series of novels written by Leslie Thomas, and was filmed in the north London suburbs of Willesden, Neasden and Harlesden.  The gentle but engrossing nature of the series was in stark contrast to other hard-hitting police dramas of the time, but this appeared to be a winning formula, becoming a surprise rating success.

Thomas &amp; Sarah: Thomas & Sarah is a British drama series that aired on ITV in 1979.  A spin-off from the BAFTA Award-winning series "Upstairs, Downstairs", it stars John Alderton and Pauline Collins reprising their "Upstairs, Downstairs" roles.

Richard Armitage (actor): Richard Crispin Armitage (born 22 August 1971) is an English film, television, theatre and voice actor.  He received notice in the UK with his first leading role as John Thornton in the British television programme "North & South" (2004).  But it was his role as dwarf prince and leader Thorin Oakenshield in Peter Jackson's film trilogy adaptation of "The Hobbit" that first brought him international recognition.  Other notable roles include John Proctor in Yaël Farber’s stage production of Arthur Miller's "The Crucible", Francis Dolarhyde in the American TV series "Hannibal", Lucas North in the British TV drama "Spooks", John Porter in the British TV drama "Strike Back", and Guy of Gisborne in the British TV drama "Robin Hood".  He more recently voiced Trevor Belmont in the Netflix adaptation of "Castlevania".

Question: English actor John Alderton plays Thomas Watkins in which British TV drama series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "character_type": {
      "type": "string",
      "description": "The type of character, e.g., fictional."
    },
    "tv_series_details": {
      "type": "array",
      "description": "Details of the TV series where the character appeared.",
      "items": {
        "type": "object",
        "properties": {
          "series_title": {
            "type": "string",
            "description": "The title of the TV series."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the TV series originated."
          }
        },
        "required": [
          "series_title",
          "country_of_origin"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "character_type",
    "tv_series_details"
  ],
  "additionalProperties": false
}
