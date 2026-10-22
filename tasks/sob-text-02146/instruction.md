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
Paul G: Paulo George Marques Joao (born March 31) better known by his stage name Paul G, is Angolan urban POP and R&B singer-songwriter, producer and dancer.  Began his career as a founding member of Angola‘s first worldly known rap group South Side Posse - SSP alongside Big Nelo, Jeff Brown, and Kudi; Then, Paul G went on to produce and guide the career of Bruna Tatiana making her the first contestant from Angola in the hit real life television show Big Brother Africa.  The success of his productions and collaborations with other artists gave him the opportunity to visit the United States of America, where he met with music producer H. Gil Ingles a founding member of XPOSURE Entertainment and that sealed his career as a solo artist with the production of the debut album ‘Transition’.

Computer Incident Advisory Capability: Computer Incident Advisory Capability (CIAC) was the original computer security incident response team at the Department of Energy.  CIAC was formed in February 1989, jointly sponsored by the DOE Office of the CIO and the Air Force.  The primary function of CIAC was, as the name implies, to advise people of computer incidents.  Primarily this means security vulnerabilities, virus and hoax alerts and similar information security concerns.  CIAC was a founding member of GFIRST, the Government Forum of Incident Response and Security Teams and FIRST, an international incident response and security organization.  CIAC published incident reports and bulletins up until it was officially renamed to DOE-CIRC and relocated to Las Vegas, Nevada in October 2008.

Tim Lambesis: Timothy Peter "Tim" Lambesis (born November 21, 1980) is an American extreme metal musician, producer, and convicted felon, best known as the founding member and lead vocalist of American metalcore band As I Lay Dying.  He also had a solo/side thrash metal project in tribute to actor Arnold Schwarzenegger, Austrian Death Machine, in which he performed all the instruments.  He also formed a death metal band called Pyrithion and played guitar for Society's Finest and Point of Recognition.

Phil Agcaoili: Phil Agcaoili (also known as philA) is a leader, technologist, entrepreneur, and accomplished cyber security, information security, and privacy expert.  He is the Chief Information Security Officer at Elavon, a Senior Vice President at U.S. Bancorp, chairman of the Ponemon Institute Fellows, a Distinguished Fellow of the Ponemon Institute, on the Board of Advisors for the Payment Card Industry (PCI) Security Standards Council (SSC), a Founding Member of the Cloud Security Alliance, co-inventor and co-author of the Cloud Security Alliance Cloud Controls Matrix (CCM), a standards developer for the Electronic Discovery Reference Model (EDRM), on the Board of Directors for Mobile Active Defense, and was on the Advisory Boards of Qualys and Rapid7.

Shadows Are Security: Shadows Are Security is the third album by American metalcore band As I Lay Dying.  The album was released on June 14, 2005 through Metal Blade Records, and was produced by Tim Lambesis, the band's vocalist, and Phil Sgrosso, one of the band's guitarists, along with Steve Russell.  A Limited Edition was released on June 23, 2005 with a bonus DVD of a show filmed at the Substage Club in Karlsruhe, Germany on November 28, 2004.  The CD was released again as a Special Edition on October 17, 2006 with a DVD on the making of the album and included videos of Confined, Through Struggle, and The Darkest Nights.  It also featured additional linear notes from vocalist Tim Lambesis on the concept of the record and little known facts on the making of the album.

Lovey (album): Lovey is the fourth studio album by the alternative rock band The Lemonheads.  It was released in 1990 on Atlantic Records.  The album was the group's first for the record company, and was the last with founding member Jesse Peretz, who would leave the band to pursue a career in photography and filmmaking.  The other founding member, Ben Deily, had left following their previous album, "Lick".

Simon Nicol: Simon John Breckenridge Nicol (born 13 October 1950) is an English guitarist, singer, multi-instrumentalist and record producer.  He was a founding member of British folk rock group Fairport Convention and is the only founding member still in the band.  He has also been involved with the Albion Band and a wide range of musical projects, both as a collaborator, producer and as a solo artist.  He has received several awards for his work and career.

Ronnie Radke: Ronald Joseph Radke (born December 15, 1983) is an American singer, songwriter, entertainer, and record producer born in Las Vegas, Nevada.  He is the founding member and current lead vocalist, keyboardist, and recently guitarist for the rock band Falling in Reverse, and is the former vocalist and founding member of post-hardcore band Escape the Fate.

The Sky Is Mine: The Sky Is Mine is a studio album by Alpha.  It was released in the United Kingdom and Europe on 18 September 2007 and released in the United States on 19 February 2008.  Founding member Andy Jenks left shortly after the sessions for the album began, leaving other founding member and producer Corin Dingley, joined by long-time Alpha vocalist Wendy Stubbs and keyboardist Peter Wild, to complete the album.

Push the Sky Away: Push the Sky Away is the fifteenth studio album by the Australian alternative rock band Nick Cave and the Bad Seeds, released on 18 February 2013 on the band's own label Bad Seed Ltd.  Recorded at La Fabrique in southern France, it is the band's first album not to feature founding member Mick Harvey, who departed the band in January 2009, and the first album to feature founding member Barry Adamson since "Your Funeral... My Trial" (1986).

Question: The producer of the album Shadows Are Security was the founding member of what band?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "album_name": {
      "type": "string",
      "description": "The name of the album in question."
    },
    "producer_details": {
      "type": "object",
      "properties": {
        "producer_name": {
          "type": "string",
          "description": "The name of the producer who was also a founding member of a band."
        },
        "founding_member_of_band": {
          "type": "string",
          "description": "The name of the band the producer was a founding member of."
        }
      },
      "required": [
        "producer_name",
        "founding_member_of_band"
      ],
      "additionalProperties": false
    },
    "album_band": {
      "type": "string",
      "description": "The band that released the album."
    }
  },
  "required": [
    "album_name",
    "producer_details",
    "album_band"
  ],
  "additionalProperties": false
}
