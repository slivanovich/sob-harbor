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
Ellen Crawford: Ellen Crawford (born April 29, 1951) is an American actress.  Most recently, she co-starred as Edith, in "The Man from Earth".  She also played Nurse Lydia Wright on ER from 1994–2003 and then again in 2009 for the series finale.  She has performed on stage as well, most recently as Nora Melody in "A Touch of the Poet" by Eugene O'Neill, for Friendly Fire Theatre in New York City.  Crawford also made a couple of guest appearances in 2010 in comedy-drama "Desperate Housewives".

Catherine Steadman: Catherine Steadman is an English actress, best known for playing Mabel Lane Fox in series 5 (2014) of ITV drama "Downton Abbey".  She also played Nurse Angela Wilson in ITV's 1960s drama "Breathless", Joan Bulmer in the final season of "The Tudors" and Maggie Lewis in the 2016 ITV miniseries "Tutankhamun".

Laura Sadler: Laura Ruth Sadler (25 December 1980 – 19 June 2003) was an English actress.  She played nurse Sandy Harper in the BBC One hospital drama series "Holby City" for three years from 2000 until her death in 2003.

Honey, I Blew Up the Kid: Honey, I Blew Up the Kid is a 1992 American comedy science fiction film and the sequel to the 1989 film "Honey, I Shrunk the Kids".  Directed by Randal Kleiser and released by Walt Disney Pictures, the film stars Rick Moranis, Marcia Strassman, Robert Oliveri and Amy O'Neill, who reprise their roles as Wayne, Diane, Nick, and Amy Szalinski respectively, as well as newcomer Keri Russell as Mandy Park, Nick's love interest and babysitter of Adam, the Szalinskis' new two-year-old son, whose accidental exposure to Wayne's new industrial-sized growth machine causes him to gradually grow to enormous size.  Made only three years after "Honey, I Shrunk the Kids", this film is set five years after the events depicted in the previous film.  It was filmed in 1991.

Eve Hewson: Memphis Eve Sunny Day Hewson (born 7 July 1991), known professionally as Eve Hewson, is an Irish actress.  Her first major role was in the drama film "This Must Be the Place" (2011).  She played Nurse Lucy Elkins in Steven Soderbergh's TV series "The Knick" (2014–2015).

Batman in film: The fictional superhero Batman, who appears in American comic books published by DC Comics, has appeared in various films since his inception.  Created by Bob Kane and Bill Finger, the character first starred in two serial films in the 1940s, "Batman" and "Batman and Robin".  The character also appeared in the 1966 film "Batman", which was a feature film adaptation of the 1960s "Batman" TV series starring Adam West and Burt Ward, who also starred in the film.  Toward the end of the 1980s, the Warner Bros. studio began producing a series of feature films starring Batman, beginning with the 1989 film "Batman", directed by Tim Burton and starring Michael Keaton.  Burton and Keaton returned for the 1992 sequel "Batman Returns", and in 1995, Joel Schumacher directed "Batman Forever" with Val Kilmer as Batman.  Schumacher also directed the 1997 sequel "Batman & Robin", which starred George Clooney.  "Batman & Robin" was poorly received by both critics and fans, leading to the cancellation of "Batman Unchained".

DuShon Monique Brown: DuShon Monique Brown (Chicago, Illinois, November 30, 1968) is an American actress.  She played Nurse Katie Welch on the Fox series "Prison Break" and Connie in "Chicago Fire".

Kathryn Apanowicz: Kathryn Apanowicz (born 3 June 1960, Horsforth, West Riding of Yorkshire) is a British actress best known for her 1980s television appearances in the BBC soap operas, "Angels", where she played Nurse Rose Butchins, and "EastEnders", where she played the caterer Magda Czajkowski.  She has also had minor roles in "Emmerdale" and "Coronation Street", and as a child appeared in the film "Bugsy Malone".  Before being cast in these shows, Apanowicz had worked in children's programmes for Yorkshire Television with Mark Curry.

Riann Steele: Riann Steele is an English actress.  After studying at Arts Educational Schools, London, she appeared in various Royal Shakespeare Company productions, including "A Midsummer Night's Dream", "Love's Labours Lost" and "Hamlet" (including its subsequent BBC television film adaptation in 2009) alongside David Tennant.  From 2009 to 2010, she played Nurse Lauren Minster in "Holby City".  Her first feature film role was opposite Aidan Gillen in 2010's "Treacle Jr.".  In 2012, she starred in the film "Sket" as Shaks, the girlfriend of a violent gang leader portrayed by Ashley Walters.  and in Doctor Who (series 7) as Queen Nefertiti.  She has also appeared as Cleo, a therapist, in the Channel 4/Netflix comedy series "Lovesick".

Marcia Strassman: Marcia Ann Strassman (April 28, 1948 – October 24, 2014) was an American actress and singer, best known for her roles as Nurse Margie Cutler on "M*A*S*H", as Julie Kotter on "Welcome Back, Kotter" and as Diane Szalinski in the feature film "Honey, I Shrunk the Kids" (1989); its sequel "Honey, I Blew Up the Kid" (1992); and the 3-D film spin-off "Honey, I Shrunk the Audience! " (1994), which was shown at several Disney theme parks through mid-2010.

Question: The actress who played nurse Margie Cutler starred in the sequel to what 1989 film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who played the specified nurse role."
    },
    "nurse_role": {
      "type": "string",
      "description": "The specific nurse role played by the actress."
    },
    "sequel_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the sequel film the actress starred in."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the sequel film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "original_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the original film to which the other film is a sequel."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the original film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "nurse_role",
    "sequel_film",
    "original_film"
  ],
  "additionalProperties": false
}
