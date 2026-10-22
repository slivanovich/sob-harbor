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
Kate Rusby: Kate Anna Rusby (born 4 December 1973) is an English folk singer-songwriter from Penistone, Barnsley.  Sometimes called the "Barnsley Nightingale", she has headlined various British national folk festivals, and is one of the best known contemporary English folk singers.  In 2001 "The Guardian" described her as "a superstar of the British acoustic scene."  In 2007 the BBC website described her as "The first lady of young folkies".  She is one of the few folk singers to have been nominated for the Mercury Prize.

Jez Lowe: Jez Lowe (born John Gerard Lowe, 14 July 1955) is an English folk singer-songwriter.  Lowe was born and raised in County Durham, in a family with Irish roots.  He is known primarily for his compositions dealing with daily life in North-East England, particularly in his hometown of Easington Colliery.  He attended St Francis RC Grammar School in nearby Hartlepool and later studied languages at Sunderland Polytechnic.  He performs both as a solo artist and with his backing band, The Bad Pennies.  In addition to singing his songs, Lowe accompanies himself and The Bad Pennies on guitar, harmonica, cittern, and piano.

List of band members in David Coverdale's bands: David Coverdale is best known for his band Whitesnake.  Whitesnake emerged when Coverdale wanted to name his backing band on tour, before becoming a device for him to promote himself with though it remained his backing band and not a band in its own right.  Later Coverdale would return to solo work and would also work with Jimmy Page on a project.  Aside from Coverdale himself, there was a number of other overlaps in membership of these various groups.  To construct an accurate chronology of his backing band therefore, the line-ups for David Coverdale Band, Whitesnake and Coverdale-Page have been included.

Charles Moothart: Charles Frances Moothart is an American multi-instrumentalist, singer and songwriter.  He is best known for his collaborations with the garage rock musicians, Ty Segall and Mikal Cronin.  Moothart is the drummer for Segall's current backing band, The Freedom Band, was the guitarist for Segall's backing band, the Ty Segall Band, and is the guitarist and vocalist in the pair's hard rock project, Fuzz.  Additionally, he is a member of Segall's collaborative project with Ex-Cult's Chris Shaw, GØGGS.

Frank Turner: Francis Edward "Frank" Turner (born 28 December 1981) is an English folk singer-songwriter from Meonstoke, Hampshire.  He began his career as the vocalist of post-hardcore band Million Dead, then embarked upon a primarily acoustic-based solo career following the band's split in 2005.  In the studio and during live performances, Turner is accompanied by his backing band, The Sleeping Souls, which consists of Ben Lloyd (guitar, mandolin), Tarrant Anderson (bass), Matt Nasir (piano) and Nigel Powell (drums).

Cat Stevens: Yusuf Islam (born Steven Demetre Georgiou, 21 July 1948 ), commonly known by his former stage name Cat Stevens, is a British singer-songwriter and multi-instrumentalist.  His 1967 debut album reached the top 10 in the UK, and the album's title song "Matthew and Son" charted at number 2 on the UK Singles Chart.

Gold Dust (Sandy Denny album): Gold Dust is a live album by the late English folk rock singer Sandy Denny.  It documents one of Denny's last public performances and was recorded at London's "Sound Circus" venue at the Royalty Theatre, Portugal Street, near Aldwych, London (now the Peacock Theatre) on 27 November 1977.  The album features many of her classic songs both as a solo artist and as a member of Fairport Convention and Fotheringay and remains the most extensive documentation of Sandy's live work with a backing band.  The album was not released on the label originally planned owing to stated technical problems with the master tape, and was only released on a different label twenty years after her death after various guitar and backing vocal tracks parts were re-recorded by Jerry Donahue and others.

Nicky Bomba: Nicholas Caruana aka Nicky Bomba (born 7 September 1963, Malta) is an Australian musician and singer-songwriter.  He is the leader of the ARIA Award-winning Melbourne Ska Orchestra, frontman of his band, Bomba, as well as the former drummer and percussionist of John Butler Trio (2003–04, 2009–13).  He has performed in other acts and as a solo artist.  His youngest sister, Danielle Caruana, (who performs as Mama Kin), is married to his former band mate, John Butler.  His older brother, Michael Caruana, is a member of Bomba and of Mama Kin's backing band.

Gerry Conway (musician): Gerald Conway (born 11 September 1947) is an English folk and rock drummer/percussionist, best known for having performed with the backing band for Cat Stevens in the 1970s, Jethro Tull during the 1980s, and currently a member of Fairport Convention as well as his side projects.  Conway has done a considerable amount of work as a session musician.

Elvis Costello: Declan Patrick MacManus (born 25 August 1954), better known by his stage name Elvis Costello, is an English musician, singer-songwriter, and record producer.  He began his career as part of London's pub rock scene in the early 1970s and later became associated with the first wave of the British punk and new wave movement that emerged in the mid-to-late 1970s.  His critically acclaimed debut album, "My Aim Is True", was released in 1977.  Shortly after recording it, he formed the Attractions as his backing band.  His second album, "This Year's Model", was released in 1978, and was ranked number 11 by "Rolling Stone" on its list of the best albums from 1967–1987.  His third album, "Armed Forces", was released in 1979, and features his highest-charting single "Oliver's Army" (number 2 in the UK).  His first three albums all appeared on "Rolling Stone"' s list of the 500 Greatest Albums of All Time.

Question: Gerald Conway, is an English folk and rock drummer/percussionist, best known for having performed with the backing band for which British singer-songwriter and multi-instrumentalist, in the 1970s, is commonly known by which former stage name

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "musician_name": {
      "type": "string",
      "description": "The name of the musician being asked about."
    },
    "musician_nationality": {
      "type": "string",
      "description": "The nationality of the musician."
    },
    "musician_role": {
      "type": "string",
      "description": "The primary role of the musician."
    },
    "associated_singer": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the associated singer-songwriter."
        },
        "former_stage_name": {
          "type": "string",
          "description": "The former stage name of the associated singer-songwriter."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the associated singer-songwriter."
        },
        "instrumentation": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Instruments the associated singer-songwriter plays."
        }
      },
      "required": [
        "full_name",
        "former_stage_name",
        "nationality",
        "instrumentation"
      ],
      "additionalProperties": false
    },
    "performance_period": {
      "type": "string",
      "description": "The decade when the musician performed with the singer's backing band."
    }
  },
  "required": [
    "musician_name",
    "musician_nationality",
    "musician_role",
    "associated_singer",
    "performance_period"
  ],
  "additionalProperties": false
}
