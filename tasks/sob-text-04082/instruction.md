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
Peter Griffen: Peter Griffen (born 1948 in Adelaide) is an Australian abstract artist.

Beatrice Mandelman: Beatrice Mandelman (December 31, 1912 – June 24, 1998), known as Bea, was a prolific American abstract artist associated with the group known as the Taos Moderns.  She was born in Newark, New Jersey to Anna Lisker Mandelman and Louis Mandelman, Jewish immigrants who imbued their children with their social justice values and love of the arts.  After studying art in New York City and being employed by the Works Progress Administration Federal Arts Project (WPA-FAP), Mandelman arrived in Taos, New Mexico, with her artist husband Louis Leon Ribak in 1944 at the age of 32.  Mandelman's oeuvre consisted mainly of paintings, prints, and collages.  Much of her work was highly abstract, including her representational pieces such as cityscapes, landscapes, and still lifes.  Through the 1940s, her paintings feature richly textured surfaces and a subtly modulated, often subdued color palette.  New Mexico landscape and culture had a profound influence on Mandelman's style, influencing it towards a brighter palette, more geometric forms, flatter surfaces, and more crisply defined forms.  One critic wrote that the "twin poles" of her work were Cubism and Expressionism.  Her work is included in many major public collections, including large holdings at the University of New Mexico Art Museum and Harwood Museum of Art.

Shimon Attie: Shimon Attie (born Los Angeles in 1957 ) is an American visual artist.  He was awarded a Guggenheim Fellowship in 2008, The Rome Prize in 2001 and a Visual Artist Fellowship from Harvard University's Radcliffe Institute for Advance Study in 2007.  His work spans a variety of media, including photography, site-specific installation, multiple channel immersive video installation, performance, and new media.  Much of Attie’s practice explores how a wide range of contemporary media may be used to re-imagine new relationships between space, time, place, and identity.  Much, though not all, of Attie’s work in the 90s dealt with the history of the second world war.  He first garnered significant international attention by slide projecting images of past Jewish life onto contemporary locations in Berlin.  More recent projects have involved using a range of media to engage local communities to find new ways of representing their history, memory and potential futures.  Attie’s artworks and interventions are site-specific and immersive in nature, and tend to engage subject matter that is both social, political and psychological.  In 2013, Five monographs have been published on Attie's work, which has also been the subject of a number of films, which have aired on PBS, BBC, and ARD.  Since receiving his MFA Degree in 1991, Attie has realized approximately 25 major projects in ten countries around the world.  Most recently, in 2013-14, Shimon Attie was awarded the Lee Krasner Lifetime Achievement Award in Art.

Ho Ho Ying: Ho Ho Ying () is a Singaporean abstract artist known for his avant-garde Chinese calligraphy and his Abstract Expressionistic works of art unique to Asian ideology.  He is also an accomplished author under his reputed moniker Zǐ Mù (子木 ), and an art critic for the Singapore visual arts community.

Kosta Bold: Kosta Bold (Kostandinos) is an American abstract artist, hand letterer, illustrator, and graphic designer.  He is best known for his Bold Brush Script, cycling art, dog art, and abstract paintings.  He is currently based in Macomb Township, Michigan.

Aelita Andre: Aelita Andre (born 9 January 2007) is an Australian abstract artist known for her Surrealist painting style and her young age.  She began to paint when aged nine months, and her work was displayed publicly in a group exhibition shortly after she turned two.  Her first solo exhibition opened in New York City in June 2011, when she was four years old.

Lindsay Edward: Lindsay M. Edward (1919-2007) was an Australian abstract artist, mosaicist and teacher.  He was born in Victoria on 26 August 1919.

Yvonne Audette: Yvonne Audette (born 1930) is a leading Australian abstract artist.

Tavar Zawacki: Tavar Zawacki is a Berlin-based international contemporary artist.  Tavar Zawacki was born in California in 1981 and has been creating public art since 1995.  Tavar Zawacki is best known for three different styles of street works, his multi-layer, full color social and political stencils, colorful abstract arrow compositions, and large text-based painted murals.  Zawacki's stencil and text-based artworks usually have a strong message or awareness about social, political, or international current events, while his abstract works are a visual language of shape, color, and form.  Tavar Zawacki began painting graffiti by tagging 'ABOVE' graffiti on freight trains in California in 1995.  At the age of 19, Tavar moved to Paris, France, where he started painting his trademark arrow icon pointing 'above'.  During the past 19 years Tavar Zawacki has painted artworks in the streets of over 100 cities in 60 different countries around the world.

Surrealism: Surrealism is a cultural movement that began in the early 1920s, and is best known for its visual artworks and writings.  Artists painted unnerving, illogical scenes with photographic precision, created strange creatures from everyday objects, and developed painting techniques that allowed the unconscious to express itself.  Its aim was to "resolve the previously contradictory conditions of dream and reality into an absolute reality, a super-reality".

Question: What type of art, best known for its visual artworks and writings, did Australian abstract artist Aelita Andre, engage in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "nationality": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "art_style": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "movement_start_period": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "description",
        "movement_start_period"
      ],
      "additionalProperties": false
    },
    "artist_known_for_style": {
      "type": "boolean"
    }
  },
  "required": [
    "artist",
    "art_style",
    "artist_known_for_style"
  ],
  "additionalProperties": false
}
