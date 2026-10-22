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
Papat Limpad 2012: Papat Limpad 2012 (English: Four Champions ) is a Javanese Language Wikipedia Revitalization Project conducted in the year 2012-2013.  Papat Limpad 2012 is a follow-up project to revitalize Javanese Wikipedia.  Learning from best practice and lessons learned in a previous project called Papat Limpad, Wikimedia Indonesia designed a combined systematic effort to do outreach with writing classes and writing drives in the form of competition in Javanese-language Wikipedia.  The project expands to three cities and approaches six universities to join the competition.  The writing classes are expected to net a group of much more experienced and smarter new editors to compete against each other, and will benefit Javanese-language Wikipedia by increasing the number of new editors and the number of high-quality Javanese-language encyclopedia articles.  The intervention is aimed at increasing the number of Javanese Wikipedia contributors up to a critical mass where the community could sustain itself and grow.  Wikimedia Indonesia believes critical mass is reached when it is sustained at a minimum of 20 very active contributors without competition.  So the success of the project can only be seen after the event.  In 2011 a similar project was done using one university intervention.  As a result, the Javanese Wikipedia readership climbed to 2.5 million readers in October 2011, and dropped back to 1.6 million in April 2012, a level similar to that of the situation before intervention happened.  Compared to Indonesian Wikipedia, where each intervention increased the readership (by/to?)  10 million and the number had the tendency to stay, until the next intervention, in a small-language Wikipedia such as Javanese Wikipedia, the readership rate dropped the minute the number of contributors dropped.

Cassandra Bankson: Cassandra Bankson (born November 11, 1992) is an American model and online personality from San Francisco, California.  She has been featured on "Good Morning America", "The Today Show", and "The Anderson Cooper Show", among other international television shows.  She has been featured in magazines including "Vogue", "Seventeen", "Glamour", "Forbes", "In Touch Weekly", "Us Weekly", and the cover of "Reveal Magazine" and newspapers "The New York Post", "The Sun", and "Pleasanton Weekly".

MKE (tabloid): MKE was a weekly publication in Milwaukee, Wisconsin published by Journal Communications.  Launched on October 28, 2004 as a zero-news-content cross between an alternative weekly and a weekly entertainment magazine aimed at readers under 35, it (along with the online version, MKEOnline.com) also served as a secondary advertising vehicle for the "Milwaukee Journal Sentinel", its parent publication.  At the time of its launch, it was seen as competing for the same readership as the "Shepherd Express".  A representative for the Association of Alternative Newsweeklies (of which the "Shepherd Express" was a member) was quoted as saying that three dozen daily newspapers had rolled out weekly free publications during the past year alone.  He characterized them as "usually pretty fluffy" and presented with "faux hipness," and said of "MKE": "Milwaukee's a little different because they've actually come out and said there's no news at all," and predicted most of the new free newspapers would fail in the long run because they lacked the "idiosyncrasies and oddball charm" of true alternative weeklies.

Style (magazine): Style was an iconic South African consumer magazine that was founded in 1981 and published by Caxton and CTP Publishers and Printers Limited.  The magazine's founding editor was Marilyn Hattingh, who based the publication on American "city magazines", aimed at an upmarket readership of conspicuous consumers.  The magazine was a highly influential chronicle of Johannesburg high society, and its tone was acerbic and often satirical.  Its content was entirely South African in origin, and the writing staff included Hilary Prendini-Toffoli, Patrick Lee, Gus Silber, Adam Levin, Chris Marais, Linda Shaw and Lin Sampson.  In late 2006, it was announced that the magazine would be discontinued.  The magazine has often been associated with a Kugel readership.

In Touch Weekly: In Touch Weekly is an American celebrity gossip magazine.  The magazine is focused on celebrity news, fashion, beauty, relationships and lifestyle, and is geared towards a younger readership, billing itself as "fast and fun", along with making claims about their lower cover price on their front cover to encourage buyers to purchase their magazine rather than the other titles on a supermarket checkout rack.

Genre (magazine): Genre magazine (ISSN 1074-5246  ) was a New York city-based monthly periodical from 1992 to 2009 written for gay men.  It was owned by gay press publisher Window Media.

Icon (lifestyle magazine): Icon magazine was a bi-monthly magazine set up in 2003 by ex-professional footballers Tim Sherwood and Jamie Redknapp as well as Redknapp's wife Louise.  The magazine was the first venture of Redknapp Publications and its readership was exclusive as it was not sold in shops and it was aimed at a celebrity readership.  Originally intended to be just for professional footballers, it branched out to many other international sports people as well as television personalities, actors and selected first class airport lounges. Official readership stood around 25,000.

Bobbie Thomas: Bobbie Thomas is the Style Editor for NBC's Today Show.  She has been considered a beauty and fashion expert for over a decade, and has appeared on TV shows including E! Red Carpet coverage, Style Network's Fashion Police, The View and Wendy Williams.  Her national column, "the Buzz" appeared in In Touch Weekly Magazine.  Now, "Bobbie's Buzz" airs weekly on TODAY with Kathie Lee Gifford and Hoda Kotb.

Justice Howard: Justice Howard (born in San Francisco, California) is an American photographer best known for her work shooting Erotica, Pin-up and Celebrities.  She really is an ""artist-without-adjective"" whose work has appeared in over 50 hardcover books and in thousands of magazines internationally including French Vogue (magazine), Esquire (magazine), Easyriders, Playboy, Cosmopolitan (magazine), People Magazine, In Touch Weekly, Skin Two, and a 25-page spread in Bound By Ink Magazine, as well as being displayed in over 60 art gallery exhibits and numerous museum shows.  She has also been featured in DANKLOOK's 'On Women in Black and White Fine Art Photography' alongside Irving Penn and Helmut Newton and is currently the favorite artist on the site.  Her photography features themes of female empowerment, freedom, and inner strength.  She was previously a model before ‘graduating to photography’ and training under a master German photographer who had previously photographed Marilyn Monroe.  Her work has been compared to Annie Leibovitz and Herb Ritts.

Dan Wakeford: Dan Wakeford (born March 3, 1975) is a journalist who covers society and celebrity news.  In 2014 he was Editor-in-Chief of In Touch Weekly.  and Life & Style Weekly

Question: are the magazines In Touch Weekly and Genre both aimed at the same readership?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "magazine_comparison_result": {
      "type": "boolean",
      "description": "Indicates whether the two magazines are aimed at the same readership."
    },
    "magazine_details": {
      "type": "array",
      "description": "Details about each magazine's target readership.",
      "items": {
        "type": "object",
        "properties": {
          "magazine_name": {
            "type": "string",
            "description": "The name of the magazine."
          },
          "target_readership": {
            "type": "string",
            "description": "Description of the magazine's target readership."
          },
          "readership_description_source": {
            "type": "string",
            "description": "The direct quote from the context describing the readership."
          }
        },
        "required": [
          "magazine_name",
          "target_readership",
          "readership_description_source"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the comparison result based on the identified readships."
    }
  },
  "required": [
    "magazine_comparison_result",
    "magazine_details",
    "reasoning"
  ],
  "additionalProperties": false
}
