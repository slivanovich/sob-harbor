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
Television in Lithuania: Television in Lithuania was introduced in 1957.  The following is a list of television channels broadcast in Lithuania.

SPT TV: SPT TV is a Portuguese language Television channel in the United States that is owned by Seabra Portuguese Television.  The channel launched in 1986 and is available via cable and satellite.  It is the first Portuguese-language television channel based in the US and features the best programming from Portugal as well as local programming created especially for the Portuguese diaspora in the US.  In January 2007, SPT TV launched SIC Notícias in North America, in partnership with SIC.  It is currently available only on Dish Network.

Canal+: Canal+ ("Canal Plus", "C+", ] , meaning "Channel Plus/More") is a French premium cable television channel launched in 1984.  It is 100% owned by the Canal+ Group, which in turn is owned by Vivendi SA.  The channel broadcasts several kinds of programming, mostly encrypted.  Unencrypted programming can be viewed free of charge on Canal+ and on satellite on Canal+ Clair (Clear).

TV6 (Poland): TV6 ("Six") is a Polish television channel, which belonged to (subsidiary of Polsat Group).  From 2014 Polsat Group is a direct broadcaster of TV6.  It was launched on 30 May 2011.  Channel was created for the second multiplex of digital terrestrial television in Poland.  The sister channel is TV4, which has existed since 2000.

Digital terrestrial television: Digital terrestrial television (DTTV or DTT) is a technological evolution of broadcast television and an advancement over analog television.  DTTV broadcasts land-based (terrestrial) signals.  The advantages of "digital" terrestrial television are similar to digital versus analog in platforms such as cable, satellite, and all telecommunications: the efficient use of spectrum and provision of more capacity than analog, better quality images, and lower operating costs for broadcast and transmission (after the initial upgrade costs).  A terrestrial implementation of digital television (DTV) technology uses an aerial to broadcast to a conventional television antenna (or aerial) instead of a satellite dish or cable television connection.

TV6 (Lithuania): TV6 is a Lithuanian terrestrial, satellite and cable television channel owned by the Nordic television company Viasat.  It was launched on March 31, 2002.  In September 15, 2008, it changed its name from Tango TV to TV6.

Drama (UK TV channel): Drama is a British digital television channel broadcasting drama (and, to a lesser extent, comedy) programming in the United Kingdom and Ireland as part of the UKTV network of channels.  The channel launched on 8 July 2013, replacing Blighty.  On Freeview, the channel was placed on channel 20, previously occupied by Gold.  On Sky, the channel initially launched on channel 291, in the overspill area of the Entertainment section and moved to channel 166 on 24 July after purchasing the slot used by PBS America.  The channel launched on Virgin Media on 14 August on channel 190.  In September 2014, UKTV blamed the channel for their 7% profits fall.

TV3 (Czech Republic): TV3 was an analogue terrestrial, cable and digital satellite television channel broadcasting in the Czech Republic.  The station used to broadcast in some regions via analogue terrestrial television to 30% of the population in the Czech Republic, cable television and also via the Czechlink platform on the Eutelsat 28A satellite.  TV3 was also planning to become part of the plans for digital terrestrial to increase its reach to 75% of the Czech Republic.  The station closed in December 2001 after its broadcast license was revoked.

Really (TV channel): Really is a British digital television channel broadcasting in the United Kingdom and Ireland as part of the UKTV family of channels.  The channel launched on 19 May 2009 as the UKTV's channel for female lifestyle programming and is available on satellite through Sky, cable services through Virgin Media also on digital terrestrial provider Freeview.

Terrestrial television: Terrestrial television or broadcast television is a type of television broadcasting in which the television signal is transmitted by radio waves from the terrestrial (Earth based) transmitter of a television station to a TV receiver having an antenna.  The term is more common in Europe, while in North America it is referred to as broadcast television or sometimes over-the-air television (OTA).  The term "terrestrial" is used to distinguish this type from the newer technologies of satellite television (direct broadcast satellite or DBS television), in which the television signal is transmitted to the receiver from an overhead satellite, and cable television, in which the signal is carried to the receiver through a cable.

Question: In what country was televison introduced in 1957 and TV6, a terrestrial satellite and cable television channel launched?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country that meets both criteria."
    },
    "television_introduction_year": {
      "type": "integer",
      "description": "The year television was introduced in the specified country."
    },
    "channel_details": {
      "type": "object",
      "properties": {
        "channel_name": {
          "type": "string",
          "description": "The name of the television channel."
        },
        "launch_date": {
          "type": "string",
          "description": "The launch date of the channel."
        },
        "broadcast_methods": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The methods by which the channel is broadcast (e.g., terrestrial, satellite, cable)."
        }
      },
      "required": [
        "channel_name",
        "launch_date",
        "broadcast_methods"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "country_name",
    "television_introduction_year",
    "channel_details"
  ],
  "additionalProperties": false
}
