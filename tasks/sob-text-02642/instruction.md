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
Jerry Vivino: Jerry Vivino (born January 8, 1954 in Paterson, New Jersey) is an American musician.  He is currently a member of the Basic Cable Band, the house band for the TBS late night program "Conan".  He was also a member of The Tonight Show Band, the house band on "The Tonight Show with Conan O'Brien" and its predecessor, "Late Night with Conan O'Brien" on NBC.

List of Conan episodes: "Conan" is a current television program on TBS hosted by Conan O'Brien.  O'Brien previously served as host of "Late Night with Conan O'Brien" for sixteen years, and as host of "The Tonight Show with Conan O'Brien" from June 1, 2009 until January 22, 2010 when the show was canceled amidst the 2010 "Tonight Show" conflict.  The conflict resulted in the former host, Jay Leno, being reinstated following the 2010 Winter Olympics on NBC, and O'Brien touring the country on his Legally Prohibited from Being Funny on Television Tour.

Late Night with Conan O'Brien: Late Night with Conan O'Brien is an American late-night talk show hosted by Conan O'Brien that aired 2,725 episodes on NBC between 1993 and 2009.  The show featured varied comedic material, celebrity interviews, and musical and comedy performances.  "Late Night" aired weeknights at 12:37 am Eastern/11:37 pm Central and 12:37 am Mountain in the United States.  From 1993 until 2000, Andy Richter served as O'Brien's sidekick; following his departure, O'Brien was the show's sole featured performer.  The show's house musical act was The Max Weinberg 7, led by E Street Band drummer Max Weinberg.

James Wormworth: James Wormworth is an American drummer and percussionist.  Wormworth is a member of Jimmy Vivino and the Basic Cable Band on the TBS late night comedy program, "Conan".  Wormworth often appeared as house drummer during the band's run as The Max Weinberg 7 on "Late Night with Conan O'Brien."  Wormworth joined the band as a full-time member when O'Brien became the host of "The Tonight Show with Conan O'Brien".

Brian Stack: Brian Stack (born August 18, 1964) is an American actor, comedian, and writer best known for his sketch comedy work on all three Conan O'Brien late-night talk shows, previously working on "Late Night with Conan O'Brien" and "The Tonight Show with Conan O'Brien", and on O'Brien's current talk show, "Conan" on TBS.  Stack left "Conan" in April 2015 to join the writing staff of the CBS series "The Late Show with Stephen Colbert".

Brian McCann (actor): Brian McCann (born August 16, 1965) is an American Emmy and WGA award-winning writer, actor, and comedian best known for his sketch comedy work on the late night talk show, "Late Night with Conan O'Brien", and more recently on "The Tonight Show with Conan O'Brien" and "Conan".

Late Night (TV series): Late Night is an American late-night talk and variety show airing on NBC since 1982.  Four men have hosted "Late Night": David Letterman (1982–93), Conan O'Brien (1993–2009), Jimmy Fallon (2009–14), and Seth Meyers (2014–present).  Each iteration of the show was built around its host, and maintained distinct identities aside from the title.  The longest-serving host to date was O'Brien, who hosted "Late Night with Conan O'Brien" for 16 years, from September 1993 to February 2009.

Andy Richter: Paul Andrew Richter (born October 28, 1966) is an American actor, writer, comedian, and late night talk show announcer.  He is best known for his role as the sidekick of Conan O'Brien on each of the host's programs: "Late Night" and "The Tonight Show" on NBC, and "Conan" on TBS.  He is also known for his work as the voice of Mort in the "Madagascar" franchise.

Jimmy Vivino: Jimmy Vivino (born January 10, 1955) is an American guitarist, keyboard player, singer, producer, and music director.  He is best known as the leader of Jimmy Vivino and the Basic Cable Band, the house band for the TBS late night program "Conan".  He was also a member of The Tonight Show Band, the house band on "The Tonight Show with Conan O'Brien" and its predecessor, "Late Night with Conan O'Brien" on NBC.  Vivino has also played with many rock bands, which most recently has included being a member of Beatles tribute band The Fab Faux.

The Tonight Show with Conan O'Brien: The Tonight Show with Conan O'Brien is an American late-night talk show that featured Conan O'Brien as host from June 1, 2009, to January 22, 2010, as part of NBC's long-running "Tonight Show" franchise.  O'Brien previously hosted NBC's "Late Night with Conan O'Brien", which followed "The Tonight Show with Jay Leno" for 16 years, until his brief succession over Leno.

Question: What member of Late Night with Conan O'Brien also did the voice of Mort in the "Madagascar" franchise? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the individual."
    },
    "role_on_late_night_show": {
      "type": "string",
      "description": "The role of the person on 'Late Night with Conan O'Brien'."
    },
    "madagascar_role": {
      "type": "string",
      "description": "The character voiced by the person in the 'Madagascar' franchise."
    },
    "madagascar_franchise_name": {
      "type": "string",
      "description": "The name of the franchise where the character was voiced."
    }
  },
  "required": [
    "person_name",
    "role_on_late_night_show",
    "madagascar_role",
    "madagascar_franchise_name"
  ],
  "additionalProperties": false
}
