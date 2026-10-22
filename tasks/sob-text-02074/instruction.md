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
The Beast on the Road: The Beast on the Road was a tour by the heavy metal band Iron Maiden, made in support of their album, "The Number of the Beast" in 1982.  It is one of Iron Maiden's longest tours to date, only surpassed in length by the World Slavery Tour, comprising 187 dates in 18 countries taking place over 10 months.

Die (album): Die!  is the sixth album by the rapper Necro.  "Die!"  was initially alluded to on Necro's MySpace profile as a "brand new solo album coming September 2009"; however, on August 13, the page's header was updated with an announcement of the album's title and its release date, which was put back to May 2010.  "Die!"  was Necro's first album since "Death Rap" in 2007 and was released by Psycho+Logical-Records.  The album's release date was finalised when the album cover was released on March 25, 2010.

This Man Must Die: This Man Must Die (French: Que la bête meure ), American title The Beast Must Die, is a 1969 French and Italian thriller film directed by Claude Chabrol.  The story is based on a 1938 novel by Cecil Day-Lewis, writing as Nicholas Blake, "The Beast Must Die".  The film had a total of 1,092,910 admissions in France.

Patrick Swayze: Patrick Wayne Swayze ( ; August 18, 1952 – September 14, 2009) was an American actor, dancer, and singer-songwriter.  Having gained fame with appearances in films during the 1980s, Swayze became popular for playing tough guys and romantic lead males, gaining him a wide fan base with female audiences, and status as a teen idol and sex symbol.

Beauty and the Beast (1987 film): Beauty and the Beast (alternatively: Cannon Movie Tales: Beauty and the Beast in United States, Die Schöne und das Biest in West Germany, La Bella e la Bestia in Italy, La Belle et la Bête in France) is a 1987 American/Israeli musical film, part of the 1980 film series Cannon Movie Tales.  It is a contemporary version of the classic tale of Beauty and the Beast.  The movie was filmed entirely in Israel, and the taglines were: ""The monster they feared was the prince she loved"" and ""The classic fairy tale about seeing with your heart"".

Forward start option: In finance, a forward start option is an option that starts at a specified future date with an expiration date set further in the future.  A forward start option starts at a specified date in the future; however, the premium is paid in advance, and the time of expiration is established at the time the forward start option is purchased.  Since the asset price at the start of this option is not known "a priori", it is common to specify that the strike price will be set in the future so that the option is initially at the money or a certain percentage in the money or out of the money.  This contract can be used to give an investor exposure to forward volatility.  Executive stock options can be viewed as a type of forward start option.  This is because a company commits to granting at-the-money options to employees in the future.

The Beast Must Die (1952 film): The Beast Must Die (Spanish: "La bestia debe morir" ) is a 1952 Argentine thriller film, which is directed by Román Viñoly Barreto and stars Guillermo Battaglia, Narciso Ibáñez Menta and Warly Ceriani.  It based on the novel The Beast must Die by Irish poet Nicholas Blake.

Deltatheridium: Deltatheridium (meaning "triangle beast" or "delta beast") is an extinct asian species of metatherian.  It lived in what is now the Gobi Desert, in Mongolia during the Upper Cretaceous, circa 80 million years ago.  It was a basal metatherian, which places it near start of the lineage that led to the marsupials, such as kangaroos, wallabies, koalas, and opossums.  The genus is featured prominently in various debates about the evolution of mammals, due to the fact that it has similarities to early versions of placental mammals.

Beast of Buchan: The Beast of Buchan is a big cat or phantom cat reportedly sighted mainly in the historic Buchan area of Aberdeenshire in northeastern Scotland.  Sightings throughout other areas of Scotland, stretching from the northern highlands down to the border with England, have also been claimed; the earliest reports date back to the 1930s.  The tales of the Buchan Beast are as well known as those of the Beast of Bodmin.

The Beast (2009 TV series): The Beast is an American crime drama series starring Patrick Swayze and Travis Fimmel.  The series, which only ran for one season, debuted on A&E Network.  It was Swayze's final acting performance before his death in 2009.  Despite receiving largely positive reviews from critics, it garnered only lukewarm viewing figures.

Question: On what date did the start of "The Beast" die?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "deceased_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who died."
        },
        "role_in_series": {
          "type": "string",
          "description": "The role of the person in the TV series 'The Beast'."
        }
      },
      "required": [
        "name",
        "role_in_series"
      ],
      "additionalProperties": false
    },
    "death_date": {
      "type": "string",
      "format": "date",
      "description": "The date of death of the person."
    },
    "related_series": {
      "type": "string",
      "description": "The name of the TV series associated with the person."
    }
  },
  "required": [
    "deceased_person",
    "death_date",
    "related_series"
  ],
  "additionalProperties": false
}
