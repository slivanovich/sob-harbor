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
French Roast: French Roast is a 2008 French computer-animated short created by Fabrice O. Joubert.  The short received ANIMA award and was nominated for Academy Award for Best Animated Short Film in 2009.

List of Uncle Grandpa episodes: This is a list of episodes for "Uncle Grandpa", an American animated TV series created by Peter Browngardt and airing on Cartoon Network.  The pilot episode was created in 2008 but was aired on Cartoon Network Video in 2010 as part of the show project "The Cartoonstitute", while the series premiered on September 2, 2013.  On July 25, 2014, the series was renewed for a second season, which premiered on March 5, 2015.

Peter Browngardt: Peter "Pete" Browngardt (born August 12, 1979 in Sag Harbor, New York) is an American animator, writer, voice actor, and producer, who is best known for being the creator of Cartoon Network's "Uncle Grandpa", in which he also voices the title character, and its early spin-off "Secret Mountain Fort Awesome".  Browngardt has had prior experience working on shows such as "Futurama", "Chowder", and "The Marvelous Misadventures of Flapjack".  His main contribution to the "Adventure Time" series is storyboarding and writing the episode "Wizard".

Adventure Time (pilot): "Adventure Time" is an animated short created by Pendleton Ward, as well as the pilot to the Cartoon Network series of the same name.  The short follows the adventures of Pen (voiced by Zack Shada), a human boy, and his best friend Jake (voiced by John DiMaggio), a dog with magical powers to change shape and grow and shrink at will.  In this episode, Pen and Jake have to rescue Princess Bubblegum (voiced by Paige Moss) from the antagonistic Ice King (voiced by John Kassir).

Secret Mountain Fort Awesome: Secret Mountain Fort Awesome is an American animated television series created by Peter Browngardt that debuted in 2011 on Cartoon Network.  The show revolves around a fraternity of five monsters who unleash wild stunts upon the public from their eponymous mountain fort.  The show is loosely based on the antagonists that appeared in Browngardt's animated short, "Uncle Grandpa", and employs Mike Conte of the heavy metal band Early Man as composer.

Regular Show (season 1): The first season of American animated television series "Regular Show" originally aired on Cartoon Network in the United States.  Many of the characters are loosely based on those developed for J.G. Quintel's student films at California Institute of the Arts: "The Naïve Man From Lolliland" and "2 in the AM PM".  Quintel pitched "Regular Show" for Cartoon Network's Cartoonstitute project, in which the network allowed young artists to create pilots with no notes to possibly be optioned as a show.  After being green-lit, Quintel recruited several indie comic book artists, plus some of the crew members he had worked with on "The Marvelous Misadventures of Flapjack", to compose the staff of the show, as their style matched close to what he desired for the series.  "Regular Show" was picked up by Cartoon Network, who decided to create a twelve-episode first season.

List of Secret Mountain Fort Awesome episodes: "Secret Mountain Fort Awesome" is an American animated television series based on the cartoon short "Uncle Grandpa" created by Peter Browngardt.  The series aired on Cartoon Network in August 1, 2011, and produced 26 episodes over two seasons.

The Cartoonstitute: The Cartoonstitute was a planned Cartoon Network project created by Cartoon Network's executive Rob Sorcher that would have been a showcase for animated shorts created without the interference of network executives and focus testing.  It was headed by Craig McCracken (creator of "The Powerpuff Girls", "Foster's Home for Imaginary Friends", and "Wander Over Yonder") and Rob Renzetti (creator of "My Life as a Teenage Robot").  39 shorts for the project were in development at Cartoon Network Studios, but only 14 of these were completed.  Eventually, balancing 5 upcoming shows and adding another proved difficult and the project was scrapped.  Of the shorts which were made, only "Regular Show" and "Uncle Grandpa" have been greenlit to become animated series (the latter was initially greenlit as "Secret Mountain Fort Awesome", before becoming a series of its own).  On May 7, 2010, Cartoon Network uploaded nearly all of the shorts to their website.  The only shorts not uploaded were "Maruined", "3 Dog Band", and "Joey to the World".

Regular Show (season 3): The third season of Emmy winning American animated television series "Regular Show" originally aired on Cartoon Network in the United States.  Many of the characters are loosely based on those developed for Quintel's student films at California Institute of the Arts: "The Naïve Man From Lolliland" and "2 in the AM PM".  Quintel pitched "Regular Show" for Cartoon Network's Cartoonstitute project, in which the network allowed young artists to create pilots with no notes to possibly be optioned as a show.  After being green-lit, Quintel recruited several indie comic book artists to compose the staff of the show, as their style matched close to what he desired for the series.  "Regular Show" was picked up by Cartoon Network, who decided to create a twelve-episode first season.

Uncle Grandpa: Uncle Grandpa is an American animated television series created by Peter Browngardt.  The series ran on Cartoon Network from September 2, 2013 to June 30, 2017.  It is based on Browngardt's animated short of the same name from "The Cartoonstitute".  "Uncle Grandpa" is also a spin-off of "Secret Mountain Fort Awesome", which was in turn a spin-off of the Cartoonstitute short.  It is produced by Cartoon Network Studios.

Question: What short created by Peter Browngardt was greenlit by The Cartoonstitute project?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the creator of the short."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "short_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the animated short film."
        },
        "creation_year": {
          "type": "integer",
          "description": "The year the pilot episode or short was created."
        }
      },
      "required": [
        "title",
        "creation_year"
      ],
      "additionalProperties": false
    },
    "cartoonstitute_project_details": {
      "type": "object",
      "properties": {
        "project_name": {
          "type": "string",
          "description": "The name of the Cartoon Network project."
        },
        "greenlit_for_series": {
          "type": "boolean",
          "description": "Indicates if the short was greenlit to become an animated series."
        },
        "initial_greenlit_series_title": {
          "type": "string",
          "description": "The title under which the short was initially greenlit as a series, if different from the short's title."
        }
      },
      "required": [
        "project_name",
        "greenlit_for_series"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "creator",
    "short_film",
    "cartoonstitute_project_details"
  ],
  "additionalProperties": false
}
