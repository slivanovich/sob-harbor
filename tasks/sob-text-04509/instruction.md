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
John McIlwraith (commentator): John McIlwraith (died June 30, 2006) was a Scottish-Canadian humorist, radio broadcaster, newspaper columnist, and commentator.

Amy Dickinson: Amy Dickinson (born November 6, 1959) is an American newspaper columnist who writes the syndicated advice column "Ask Amy".  Dickinson has appeared as a social commentator on ABC's "Good Morning America" and NBC's "The Today Show".

George Dunn (actor): George Dunn (November 23, 1914 – April 27, 1982) was an American actor, humorist, vaudeville performer, and satirist.  He often portrayed Western characters in film and television.  His homespun wit, rope tricks, and satirizing of American life, politics, and sports reflected the strong influence Will Rogers had on him as an entertainer.

Jon Gaunt: Jonathan Charles Gaunt (born 3 March 1961 in Coventry) is an English radio talk show presenter, TV personality, newspaper columnist, social commentator and spokesman.

Robert North: Robert North (or Bobby North; February 2, 1884 – August 13, 1976) was an American vaudeville performer who became a success as a stand-up comedian.  Later he became a prolific motion picture producer.

Will Rogers: William Penn Adair "Will" Rogers (November 4, 1879 – August 15, 1935) was a stage and motion picture actor, vaudeville performer, American cowboy, humorist, newspaper columnist, and social commentator.

William &quot;Bill&quot; Hanley: William D. Hanley (February 8, 1861 – September 15, 1935), known as Bill Hanley, was a pioneer rancher in Harney County in southeastern Oregon.  He owned several ranches between Burns, Oregon and Harney Lake.  Together, his properties comprised one of the largest privately owned cattle operations in the United States.  Hanley was also a progressive thinker and well known host.  Among his personal friends were leading political figures, fellow cattle barons, industrialist, writers, and artists including Theodore Roosevelt, William Howard Taft, William Jennings Bryan, Peter French, James J. Hill, CES Wood, and Will Rogers.  Hanley’s progressive political views led him to run for Governor of Oregon and the United States Senate.  A strong advocate of wildlife conservation, much of his ranch is now part of the Malheur National Wildlife Refuge.

Tom Mix filmography: Tom Mix (1880–1940) was an American motion picture actor, director, and writer whose career spanned from 1910 until 1935.  During this time he appeared in 270 films and established himself as the screen's most popular cowboy star.  Mix's flair for showmanship set the standard for later cowboy heroes such as Gene Autry and Roy Rogers.  His horse Tony also became a celebrity who received his own fan mail.

Vaudeville: Vaudeville ( ; ] ) is a theatrical genre of variety entertainment.  It was especially popular in the United States and Canada from the early 1880s until the early 1930s.  A typical vaudeville performance was made up of a series of separate, unrelated acts grouped together on a common bill.  Types of acts have included popular and classical musicians, singers, dancers, comedians, trained animals, magicians, strongmen, female and male impersonators, acrobats, illustrated songs, jugglers, one-act plays or scenes from plays, athletes, lecturing celebrities, minstrels, and movies.  A vaudeville performer is often referred to as a "vaudevillian".

Audrey Stubbart: Audrey Stubbart (June 9, 1895–November 13, 2000) was an American centenarian who worked as a proofreader and newspaper columnist for "The Independence Examiner" until the age of 105.  Prior to her death she was the oldest verified newspaper columnist, the oldest known full-time employee, and possibly the oldest user of the Internet.

Question: What personal friend of William "Bill" Hanley was a stage and motion picture actor, vaudeville performer, American cowboy, humorist, newspaper columnist, and social commentator?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person who was a friend of William 'Bill' Hanley."
    },
    "is_friend_of_bill_hanley": {
      "type": "boolean",
      "description": "Indicates if the person was a personal friend of William 'Bill' Hanley."
    },
    "professions": {
      "type": "array",
      "description": "A list of professions held by the person.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "person_name",
    "is_friend_of_bill_hanley",
    "professions"
  ],
  "additionalProperties": false
}
