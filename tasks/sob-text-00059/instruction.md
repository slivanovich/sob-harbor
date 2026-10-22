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
William Schoell: William Schoell (pronounced "shoal") is an American author, biographer and film historian, born in Manhattan in 1951 and educated in Vermont, earning a B.A. from Castleton State College.  He has written several horror and science fiction novels, such as "Late at Night" (1986) and "Saurian" (1988).  He was the author of "Hidden Horrors," a column in the now defunct horror magazine "The Scream Factory", as well as a contributor of articles and reviews to periodicals including "Writer", "Writer's Digest", "Paris Notes", "Off Duty", and "BBC Music".  He was also a talk show radio host and producer.  More recently, he has published books that deal with film, and biographies, some of which were written together with Hollywood biographer Lawrence J. Quirk, his domestic partner.  His play "Joe and Janice" premiered at the American Theater of Actors in 2000.  He writes a popular blog on movies called Great Old Movies.  Prominent in the Gay Rights Movement in the 1970s, he now has a blog called "Ask Gay "Dr." Bill," which answers questions about gay life and the LGBT community.

Video blog: A video blog or video log, usually shortened to vlog , is a form of blog for which the medium is video, and is a form of web television.  Vlog entries often combine embedded video (or a video link) with supporting text, images, and other metadata.  Entries can be recorded in one take or cut into multiple parts.  The vlog category is popular on YouTube.

Christina Hoff Sommers: Christina Marie Hoff Sommers (born September 28, 1950) is an American author and philosopher.  She is a resident scholar at the American Enterprise Institute (AEI), a conservative think tank.  Sommers is known for her critique of contemporary feminism.  Her work includes the books "Who Stole Feminism? " (1994) and "The War Against Boys" (2000), and her writing has been featured in a variety of different media outlets, including "The New York Times", "Time" magazine, and "The Atlantic".  She also hosts a video blog called "The Factual Feminist".

Rosie O'Donnell: Roseann O'Donnell (born March 21, 1962) is an American comedian, actress, author, and television personality.  She has been a magazine editor and continues to be a celebrity blogger, a lesbian rights activist, a television producer, and a collaborative partner in the LGBT family vacation company, R Family Vacations.

Jahero: JaHeRo is the video blog (vlog) started by Rosie O'Donnell on her website Rosie.com answering fans questions, giving behind the scenes information and serving as a video diary.  Originally featuring only O'Donnell and her hair and make-up artist Helene Macaulay they were soon joined by her writer from "The Rosie O'Donnell Show", Janette Barber.  O'Donnell, her producer Barber, and Macaulay created unscripted video blogs Monday through Thursday prior to taping, during which they answered user-submitted questions.  Called "Jahero", composed of the first two letters of each of their first names, they occasionally had short cameo appearances by "View" co-hosts Joy Behar, Elisabeth Hasselbeck, and Barbara Walters.  Jenny McCarthy appeared once briefly, as has Hasselbeck's mother-in-law and O'Donnell's mother-in-law, her wife Kelli's mother.  Kathy Griffin also appeared, where she read some of the questions.  It became so popular that O'Donnell and her creative team considered an "on the road" version of the video blog utilizing fan-submitted suggestions.  O'Donnell was the front runner for the "best celebrity blogger" category in the 2007 Blogger's Choice Awards which she won.

Sofi Fahrman: Sofi Margareta Fahrman (born July 20, 1979, in Stockholm) is a Swedish journalist and fashion reporter for the Aftonbladet newspaper.  She runs and owns the blog Sofis Mode on the Aftonbladets official website, and publishes her own fashion magazine, "Sofis mode", as a supplement to the Aftonbladet newspaper each week.  Fahrman also runs a blog called Sofis snapshots.  Before starting "Sofis mode" she was a celebrity editor for Aftonbladets celebrity and entertainment magazine "Klick!" .  She currently resides in New York.

The Comics Curmudgeon: The Comics Curmudgeon is a blog devoted to humorous and critical analysis of newspaper comics.  Its author, Josh Fruhlinger, is a freelance writer and editor based in Los Angeles.  Fruhlinger, formerly based in Baltimore, also writes about editorial cartoons for the website Wonkette in a weekly feature called "Cartoon Violence".  He also contributes to a Wikipedia-themed humor blog called Citation Needed.

IsRealli: IsRealli is the official blog of the State of Israel and the first official blog to ever be started by a government.  Originally called Israel Video Blog, the site was launched on February 16, 2006 by the Consulate General of Israel in New York.  In October 2006, the blog was relaunched as isRealli, with the tagline, “The New Blog of Israel.”  This was the first initiative by the Israeli Consulate in New York City in Public Diplomacy 2.0.  Following the success of isRealli, the Consulate launched a series of new media projects including a MySpace page, YouTube site, political blog, and Twitter press conference, which was widely reported by news media around the world.  isRealli is maintained on a daily basis by the media and public affairs team at the Consulate General of Israel in New York.

Michelle Slatalla: Michelle Slatalla is an American journalist.  The editor in chief of the blog "Gardenista", she was previously a reporter for "Newsday" and a columnist for "The New York Times", and "TIME magazine."  One of the first columnists at "The New York Times" to write weekly about parenting and child rearing, she made her family the subject of much of her work, an approach that in the mid-2000s prompted criticism from a younger generation of bloggers at "Gawker" .  She is also the author or co-author of several books, and in 2012 became a blogger herself as editor-in-chief of a lifestyle blog called Gardenista.

Citizen Kate: Citizen Kate is a continuing web series and video blog about Citizen journalism.  In 2008, when the series was first created by Carey Lundin of Viva Lundin Productions, "Kate Soglin, a young "citizen journalist," gave the outsider’s view of inside politics.  Citizen Kate was one of the first Citizen Journalists to hit the 2008 presidential campaign trail.  She started her video blog coverage on February 10, 2007 at Barack Obama's announcement to run for president in Springfield, Illinois.  She has filed several vblogs about the presidential campaign and politics on her web site CitizenKate.tv.

Question: What American comedian has been a magazine editor and has a video blog called JaHeRo on her website?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The full name of the person."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the person."
    },
    "occupation_types": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of occupations held by the person."
    },
    "has_been_magazine_editor": {
      "type": "boolean",
      "description": "Indicates if the person has been a magazine editor."
    },
    "video_blog_details": {
      "type": "object",
      "properties": {
        "blog_name": {
          "type": "string",
          "description": "The name of the video blog."
        },
        "blog_platform": {
          "type": "string",
          "description": "The platform where the video blog is hosted."
        },
        "blog_url_part": {
          "type": "string",
          "description": "The specific website part or domain for the blog."
        },
        "blog_purpose": {
          "type": "string",
          "description": "The main purpose or content of the video blog."
        },
        "blog_creators": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of individuals who created or regularly featured in the blog."
        }
      },
      "required": [
        "blog_name",
        "blog_platform",
        "blog_url_part",
        "blog_purpose",
        "blog_creators"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "nationality",
    "occupation_types",
    "has_been_magazine_editor",
    "video_blog_details"
  ],
  "additionalProperties": false
}
