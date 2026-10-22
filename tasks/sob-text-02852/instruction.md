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
2014 MTV Europe Music Awards: The 2014 MTV EMAs (also known as the MTV Europe Music Awards) were held at The SSE Hydro, Glasgow, Scotland on 29 September 2014.  Bruce Gillmer, from Viacom International Media Network (VIMN), confirmed the ceremony would be held in Glasgow for the first time.  This was the first time since 2003 when the awards were held in Scotland and the fifth time the United Kingdom has hosted the MTV EMA since the show was hosted in Belfast, Northern Ireland.  The event showcases the world's hottest musical acts in a different city each year.  The event was hosted by Nicki Minaj.

2017 MTV Europe Music Awards: The 2017 MTV EMAs (also known as the MTV Europe Music Awards) will be held at The SSE Arena in Wembley, London, United Kingdom, on 12 November 2017.  The host of this ceremony is Rita Ora.  This will be the sixth time that the UK has hosted the awards show, and the second time London has been the host city.  London first hosted the awards ceremony in 1996 at Alexandra Palace.

2013 MTV Europe Music Awards: The 2013 MTV EMAs (also known as the MTV Europe Music Awards) were held at the Ziggo Dome, Amsterdam, Netherlands, on 31 August 2013.  This was the second time the awards had taken place in the Netherlands, the last time being in 1997.

2015 MTV Europe Music Awards: The 2015 MTV EMAs (also known as the MTV Europe Music Awards) were held at the Mediolanum Forum in Assago, near Milan, Italy, on 22 September 2015.  This was the third time the awards have taken place in Italy, second time Assago has been the host city, and the first time that the awards have been held in October.  The awards was held in the same venue as the 1998 MTV EMAs.  On 30 September 2015, it was announced that singer Ed Sheeran would host the awards, along with actress Ruby Rose.

2016 MTV Europe Music Awards: The 2016 MTV EMAs (also known as the MTV Europe Music Awards) were held at the Rotterdam Ahoy in Rotterdam, Netherlands, on 16 September 2016.  It was hosted by Bebe Rexha.  This was the third time the awards have taken place in the Netherlands, and the second time Rotterdam has been the host city.  The awards were held in the same venue as the 1997 MTV EMAs.

Ruby Rose: Ruby Rose Langenheim (born 20 March 1986), better known as Ruby Rose, is an Australian model, DJ, recording artist, actress, television presenter, and former MTV VJ.  Rose emerged in the media spotlight as a presenter on MTV Australia, followed by several high-profile modelling gigs, notably as the face of Maybelline New York in Australia.  In addition to her modelling career, she has co-hosted various television shows, namely "Australia's Next Top Model" and "The Project" on Network Ten.

MTV Europe Music Award: The MTV Europe Music Awards ("EMAs" or "EMA") is an event presented by MTV Networks Europe which awards prizes to musicians and performers.  Since 2007, the winners are chosen by the viewers and fans by visiting the EMAs' website.  The first EMAs ceremony was held in 1994 in Berlin, Germany.

2012 MTV Europe Music Awards: The 2012 MTV EMAs (also known as the MTV Europe Music Awards) were held in Frankfurt, Germany, on 26 August 2012.  This was the fifth time the awards had been held in Germany, and the second time Frankfurt had been the host city.  On 17 August the nominees were announced.  Rihanna received eight nominations while Katy Perry and Taylor Swift received five, leading the categories.

2008 MTV Europe Music Awards: The 2008 MTV EMAs (also known as the MTV Europe Music Awards) were held at the Echo Arena in Liverpool, England, on 27 September 2008.  It was hosted by Katy Perry.  This was the second time the awards have taken place in England.

2011 MTV Europe Music Awards: The 2011 MTV EMAs (also known as the MTV Europe Music Awards) were held in Northern Ireland's capital Belfast, on Saturday, September 24, 2011, at the Odyssey Arena in the Titanic Quarter area of the city and were hosted by Selena Gomez and Paul Clark.  Additional live venues for the awards show include Ulster Hall and Belfast City Hall.

Question: Which Australian Model co-hosted the 1998 MTV EMAs alongside with Ed Sheeran?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "host_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the Australian model who co-hosted."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the host."
        },
        "profession": {
          "type": "string",
          "description": "The primary profession of the host as specified in the question."
        }
      },
      "required": [
        "name",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    },
    "co_host_name": {
      "type": "string",
      "description": "The name of the co-host mentioned in the question."
    },
    "event_hosted_year": {
      "type": "integer",
      "description": "The actual year the identified individuals co-hosted the MTV EMAs, according to the context."
    }
  },
  "required": [
    "host_details",
    "co_host_name",
    "event_hosted_year"
  ],
  "additionalProperties": false
}
