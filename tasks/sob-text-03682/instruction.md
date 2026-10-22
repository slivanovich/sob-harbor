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
BP Portrait Award: The BP Portrait Award is an annual portraiture competition held at the National Portrait Gallery in London, England.  It is the successor to the John Player Portrait Award.  It is the most important portrait prize in the world, and is reputedly one of the most prestigious competitions in contemporary art.  The "Daily Mail" has called it "the portraiture Oscars".

National Portrait Gallery, London: The National Portrait Gallery (NPG) is an art gallery in London housing a collection of portraits of historically important and famous British people.  It was the first portrait gallery in the world when it opened in 1856.  The gallery moved in 1896 to its current site at St Martin's Place, off Trafalgar Square, and adjoining the National Gallery.  It has been expanded twice since then.  The National Portrait Gallery also has regional outposts at Beningbrough Hall in Yorkshire and Montacute House in Somerset.  It is unconnected to the Scottish National Portrait Gallery in Edinburgh, with which its remit overlaps.  The gallery is a non-departmental public body sponsored by the Department for Culture, Media and Sport.

Johann Jakob Dorner the Elder: Johann Jakob Dorner the Elder, who was born at Ehrenstetten, near Freiburg in Breisgau, in 1741, was at first a pupil of Rösch at Freiburg and of Ignaz Bauer at Augsburg.  He afterwards visited Italy, the Netherlands, and Paris; and excelled as a painter of historical and genre subjects.  He was a professor and director of the Gallery at Munich in 1770, and died in that city in 1813.  In the Darmstadt Gallery is a picture of 'Two Soldiers and a Maiden' by him; and in the Pinakothek at Munich, a 'Linen Draper,' which is a portrait of his wife, dated 1775.

Streatham portrait: The "Streatham" portrait is an oil painting on panel from the 1590s believed to be a later copy of a portrait of the English noblewoman Lady Jane Grey dating to her lifetime (1536/1537–54).  It shows a three-quarter-length depiction of a young woman in Tudor-period dress holding a prayer book, with the faded inscription "Lady Jayne" or "Lady Iayne" in the upper-left corner.  It is in poor condition and damaged, as if it has been attacked.  Although of historical interest, it is generally considered to be of poor artistic quality.  s of January 2015 the portrait is in Room 3 of the National Portrait Gallery in London.

Portrait of Lucrezia Panciatichi: The Portrait of Lucrezia Panciatichi is a painting by the Italian artist Agnolo di Cosimo, known as Bronzino, finished around 1545.  It is housed in the Uffizi Gallery in Florence, Italy.

Art Treasures Exhibition, Manchester 1857: The Art Treasures of Great Britain was an exhibition of fine art held in Manchester, England, from 5 May to 17 October 1857.  It remains the largest art exhibition to be held in the UK, possibly in the world, with over 16,000 works on display.  It attracted over 1.3 million visitors in the 142 days it was open, about four times the population of Manchester at that time, many of whom visited on organised railway excursions.  Its selection and display of artworks had a formative influence on the public art collections that were then being established in the UK, such as the National Gallery, National Portrait Gallery and the Victoria and Albert Museum.

Uffizi: The Uffizi Gallery (Italian: Galleria degli Uffizi , ] ) is a prominent art museum located adjacent to the Piazza della Signoria in the Historic Centre of Florence in the region of Tuscany, Italy.  One of the most important Italian museums, and the most visited, it is also one of the largest and best known in the world, and holds a collection of priceless works, particularly from the period of the Italian Renaissance. 

Edward Savage (artist): Edward Savage (November 26, 1761 in Princeton, Massachusetts – July 6, 1817 in Princeton, Massachusetts) was an American portrait painter and engraver.  He was born in Princeton, Mass., and at first worked as a goldsmith, also practicing engraving.  Although seemingly untrained in painting, he came into prominence in 1790 through his portrait of George Washington, intended as a gift to Harvard University.  In 1791 he visited London, where he studied for a time under Benjamin West, and then went to Italy.  Upon his return to the United States in 1794, he practiced in Philadelphia and New York City, maintaining for several years a picture gallery and art museum on Water Street in New York.

Portrait of Eleanor of Toledo: The Portrait of Eleanor of Toledo and Her Son is a painting by the Italian artist Agnolo di Cosimo, known as Bronzino, finished ca. 1545.  One of his most famous works, it is housed in the Uffizi Gallery of Florence, Italy and is considered one of the preeminent examples of Mannerist portraiture.  The painting depicts Eleanor of Toledo, the wife of Cosimo I de' Medici, Grand Duke of Tuscany, sitting with her hand resting on the shoulder of one of her sons.  This gesture, as well as the pomegranate motif on her dress, referred to her role as mother.  Eleanor wears a heavily brocaded dress with black arabesques.  In this pose, she is depicted as the ideal woman of the Renaissance.  The painting is the first known state-commissioned portrait to include the ruler's heir.  By including the child, Cosimo wished to imply that his rule would bring stability to the duchy.

Portrait of Bartolomeo Panciatichi: The Portrait of Bartolomeo Panciatichi is a painting by the Italian artist Agnolo di Cosimo, known as Bronzino, finished around 1540.  It is housed in the Uffizi Gallery of Florence, Italy.

Question: In which town in Tuscany can you find a gallery, considered the most important and most visited, which houses the Portrait of Lucrezia Panciatichi?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "gallery_name": {
      "type": "string",
      "description": "The name of the art gallery."
    },
    "city": {
      "type": "string",
      "description": "The city where the gallery is located."
    },
    "region": {
      "type": "string",
      "description": "The region where the gallery is located."
    },
    "painting_housed": {
      "type": "string",
      "description": "The name of the painting housed in the gallery."
    },
    "gallery_description": {
      "type": "string",
      "description": "A description of the gallery's importance or visitor numbers."
    }
  },
  "required": [
    "gallery_name",
    "city",
    "region",
    "painting_housed",
    "gallery_description"
  ],
  "additionalProperties": false
}
