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
Aileen Wuornos: Aileen Carol Wuornos Pralle (February 29, 1956 – October 9, 2002) was an American serial killer who murdered seven men in Florida between 1989 and 1990 by shooting them at point-blank range.  Wuornos claimed that her victims had either raped or attempted to rape her while she was working as a sex worker, and that all of the homicides were committed in self-defense.  She was convicted and sentenced to death for six of the murders and was executed by lethal injection on October 9, 2002.

Phillip Carl Jablonski: Phillip Carl Jablonski (born January 3, 1946) is an American serial killer convicted of killing five women in California and Utah between 1978 and 1991.

Gary Ridgway: Gary Leon Ridgway (born February 18, 1949) is an American serial killer known as the Green River Killer.  He was initially convicted of 48 separate murders and is presumed to be responsible for more than 90.  As part of his plea bargain, an additional conviction was added, bringing the total number of convictions to 49, making him the most prolific American serial killer in history according to confirmed murders.  He murdered numerous women and girls in Washington State during the 1980s and 1990s.

Cody Legebokoff: Cody Alan Legebekoff (born  1990 ) is a Canadian serial killer convicted in 2014 by the British Columbia Supreme Court of murdering three women and a teenage girl, between 2009 and 2010, in or near the City of Prince George, British Columbia.  This trial of one of Canada's youngest serial killers drew national attention.

Randy Steven Kraft: Randy Steven Kraft (born March 19, 1945) is an American serial killer known as the "Scorecard Killer" and the "Freeway Killer" who committed the rape, torture, mutilation, and murder of a minimum of 16 young men in a series of killings spanning between 1972 and 1983, the majority of which had been committed in California.  Kraft is also believed to have committed the rape and murder of up to 51 further boys and young men.  He was convicted in May 1989 of murdering 16 victims and is currently incarcerated upon death row at San Quentin State Prison in Marin County, California.

Michael Hughes (serial killer): Michael Hughes (born c. 1956) is an American serial killer convicted and sentenced to life without parole for the murders of four women and girls in California, and later, in another trial, sentenced to death for the murders of three other women.

Larry Eyler: Larry Eyler (December 21, 1952 – March 6, 1994) was an American serial killer convicted and sentenced to death in Illinois for the 1984 murder and dismemberment of 15-year-old Daniel Bridges.

Monster (2003 film): Monster is a 2003 biographical crime drama film written and directed by Patty Jenkins.  The film is about serial killer Aileen Wuornos, a former prostitute who was executed in Florida in 2002 for killing six men (she was not tried for a seventh murder) in the late 1980s and early 1990s.  Wuornos was played by Charlize Theron, and her semi-fictionalized lover, Selby Wall (based on Wuornos's real-life girlfriend Tyria Moore), was played by Christina Ricci.

Carlton Gary: Carlton Michael Gary (born September 24, 1950) is an American serial killer convicted of the murders of elderly women in Columbus, Georgia from 1977-1978.

John Joubert (serial killer): John Joseph Joubert IV (July 2, 1963 – July 17, 1996) was an American serial killer convicted of the murders of three boys in Maine and Nebraska.  He was executed in Nebraska.

Question: How many men was this American serial killer convicted of murdering who became the subject of the 2003 biographical crime drama film "Monster?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "serial_killer_name": {
      "type": "string",
      "description": "The name of the serial killer who was the subject of the film."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the biographical crime drama film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "convicted_murders_count": {
      "type": "integer",
      "description": "The number of murders the serial killer was convicted of."
    },
    "victim_gender": {
      "type": "string",
      "description": "The gender of the victims for which the serial killer was convicted."
    }
  },
  "required": [
    "serial_killer_name",
    "film_title",
    "film_release_year",
    "convicted_murders_count",
    "victim_gender"
  ],
  "additionalProperties": false
}
