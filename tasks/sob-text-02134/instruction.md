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
Mary and Max: Mary and Max is a 2009 Australian stop motion animated comedy-drama film written and directed by Adam Elliot as his first animated feature film with music by Dale Cornelius and produced by Melanie Coombs and Melodrama Pictures.  The voice cast included Philip Seymour Hoffman, Toni Collette, Eric Bana, Bethany Whitmore with narration by Barry Humphries.  The film premiered on the opening night of the 2009 Sundance Film Festival on January 15, 2009.  The film won the Annecy Cristal in June 2009 from the Annecy International Animated Film Festival, and Best Animated Feature Film at the Asia Pacific Screen Awards in November 2009.  The film was theatrically released on April 9, 2009 by Icon Entertainment International.  "Mary and Max" received very positive reviews from critics and it earned $1.7 million USD on a $8.2 million AUD budget.

Etiuda&amp;Anima International Film Festival: The International Film Festival "Etiuda&Anima" (Polish: "Międzynarodowy Festiwal Filmowy Etiuda&Anima" ), is the leading animation film festival in Poland organized in Kraków continuously since 1994, and catering to independent producers, animation films professionals, and students of film and art schools from all over the world.  Since 2010 the festival has also included workshops in scriptwriting, directing, cinematography, editing and animation, led by renown artists and pedagogues from foreign film schools.  The main two events of each festival are the actual competitions awarding the Golden, Silver and Bronze Dinosaur' prizes in two categories (hence the name, Etiuda & Anima) including feature and documentary etudes as well as (since 2005) experimental filmography.  The Special Golden Dinosaur Award is presented to the best film school of the festival.  In the "Anima" part of the contest, Golden, Silver and Bronze Jabberwocky are awarded, with Special Golden Jabberwocky reserved for the best animated etude of the festival.  The annual Special Golden Dinosaur is awarded to an outstanding artist turned pedagogue.

Diane Michelle: Diane Michelle is an American voice actress, famous for voicing Daisy Duck in several modern Disney projects (Daisy is currently voiced by Tress MacNeille in many projects) in The Spirit of Mickey, Mickey Mouse Works and Mickey's Once Upon a Christmas.

Alê Abreu: Alê Abreu (born March 6, 1971) is a Brazilian film director and screenwriter.  "Sírius", his first short film, debuted at the 1993 Anima Mundi as the only Brazilian animation that year.  It won the Best Film Award at the Festival de Cine para Niños y Jovenes and was also screened at the Mostra Internacional de Cinema São Paulo and at the section Animation for Children of the Hiroshima International Animation Festival.  His second short film, "Espantalho" (lit.  "Scarecrow"), released in 1998, won the 3rd Best Brazilian Animation at the Anima Mundi, the Best Art Direction Award at the Brazilian Film Festival of Miami, and was nominated for Best Animated Feature at the 1st Grande Prêmio Cinema Brasil.  His first feature film, "Garoto Cósmico", debuted at the 2007 Anima Mundi.  In 2013, he released "The Boy and the World", his second film, at the Ottawa International Animation Festival which won the Grand Prix for best feature film at World Festival of Animated Film - Animafest Zagreb in 2015.

Chasing Shakespeare: Chasing Shakespeare is a 2013 film directed by Norry Niven, and starring Danny Glover, Ashley Bell, and Graham Greene.  The premiered at the Dallas International Film Festival Festival in April 2013, and was opening night film at the Breckenridge Film Festival, The Montreal Black Film Festival, The 38th annual Native American Film Festival in San Francisco on November 1, 2013, The African Diaspora Film Festival NY and The Orlando Film Festival.  It has been nominated 36 times in as many festivals, winning 27 awards including Best Feature Film at The FirstGlance Film Festival, Best of Fest at The Big Island Film Festival, Best Feature Film at the AFI Cannes Film Festival, Audience Choice, Best Opening Title Sequence at SXSW, Best Dram/Romance at The WorldFest Houston Film Festival, Best Feature Film at the World Peace Initiative The Hampton's Film Festival and Best Director at Red Nations Film Festival and The Orlando Film Festival.  The film was written by James Bird.

A Monkey's Tale: A Monkey's Tale (French: Le Château des singes ; literally "The Castle of Monkeys") is a feature-length French animated film directed by Jean-François Laguionie.  It was released in 1999, and won the Award for Best Animated Feature Film at the 5th Kecskemét Animation Film Festival.  It has never been released on American video or DVD, although it has been available in the United Kingdom.

Kecskemét Animation Film Festival: Kecskemét Animation Film Festival (Hungarian: "Kecskeméti Animációs Filmfesztivál" ) (KAFF) is an animated film festival held biennially during the month of June in Kecskemét, Hungary.  Although the bulk of the festival is oriented toward efforts in Hungarian animation, the associated KAFF-sponsored Festival of European Animated Feature Films and TV Specials (Hungarian: "Európai Animációs Játékfilm Fesztivál" ) has opened the festival to international works as well.  The festival was first held in 1985 and was opened to international works of animation in 1996.

Mickey's Once Upon a Christmas: Mickey's Once Upon a Christmas is a 1999 direct-to-video animated Christmas anthology film produced by Walt Disney Home Video and won the Award for Best Animated Feature Film at the 5th Kecskemét Animation Film Festival in 1999.  The video features Mickey Mouse, Minnie Mouse, Pluto, Pete, Goofy, Max, Donald Duck, Daisy Duck, Huey, Dewey and Louie, Scrooge McDuck, Mortimer Mouse, Figaro the Kitten and Chip 'n Dale with cameos by Owl, Clarabelle Cow, Horace Horsecollar, and a Beagle Boy.  The film comprises three separate segments, with narration by Kelsey Grammer.  A sequel, titled "Mickey's Twice Upon a Christmas", was released in 2004.

Tarzan &amp; Jane: Tarzan & Jane is an animated comedy-adventure film produced by Walt Disney Television Animation, Toon City and Walt Disney Animation Australia released on July 23, 2002 and a direct-to-video sequel to the Disney's 1999 animated feature "Tarzan", and uses three unaired episodes of the film's corresponding television series, "The Legend of Tarzan". " Tarzan II", a followup to the original film, was released in 2005.  The film is set one year after the events of the first film.

Ferenc Mikulás: Ferenc Mikulás (17 August 1940, Dunapataj) is a figure in the Hungarian animation film culture.  He is the founder and director of the animation film studio Kecskemétfilm Kft., and the director of Kecskemét Animation Film Festival (KAFF).

Question: Which 1999 Animated Feature Film winner at the 5th Kecskemet Animation Film Festival featured the voice of American voice actress Diane Michelle?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the animated feature film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "award_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the award won by the film."
        },
        "festival_name": {
          "type": "string",
          "description": "The name of the film festival where the award was received."
        },
        "festival_edition": {
          "type": "integer",
          "description": "The edition number of the film festival."
        },
        "award_year": {
          "type": "integer",
          "description": "The year the award was given."
        }
      },
      "required": [
        "award_name",
        "festival_name",
        "festival_edition",
        "award_year"
      ],
      "additionalProperties": false
    },
    "voice_actress_details": {
      "type": "object",
      "properties": {
        "actress_name": {
          "type": "string",
          "description": "The name of the American voice actress featured in the film."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the voice actress."
        },
        "character_voiced": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The character(s) voiced by the actress in this film."
        }
      },
      "required": [
        "actress_name",
        "nationality",
        "character_voiced"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "award_details",
    "voice_actress_details"
  ],
  "additionalProperties": false
}
