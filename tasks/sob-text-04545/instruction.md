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
List of Albanian Air Force aircraft: Albanian military aircraft include all airplanes and helicopters which have been operated by the Albanian Air Force since its formal inception in 1947.  Since the small country of Albania has no domestic aircraft manufacturing capacity, all aircraft have been procured from other countries.  Additionally, the country's limited resources have meant that such procurement has been primarily through foreign military aid provided to Albania for strategic reasons.  Initially, the Warsaw Pact provided equipment through the 1950s, but after a political rift, China supplanted them as the country's main benefactor.  After the end of the Cold War and a significant shift in Albanian international relations, as well as a re-posturing of the Albanian Armed Forces, the air force has sought more modern support helicopters from Western Europe to support its new role in partnership with NATO.

Unpowered aircraft: Unpowered aircraft can remain airborne for a significant period of time without onboard propulsion.  They can be classified as fixed-wing gliders, lighter-than-air balloons and tethered kites.  This requires a trajectory that is not merely a vertical descent such as a parachute.  In the case of kites, lift is obtained by tethering to a fixed or moving object, perhaps another kite, to obain a flow of wind over the lifting surfaces.  In the case of balloons, lift is obtained through inherent buoyancy and the balloon may or may not be tethered.  Free balloon flight has little directional control.  Gliding aircraft include sailplanes, hang gliders, and paragliders that have full directional control in free flight.

Fractional ownership of aircraft: Fractional Aircraft is a common term for fractional ownership of aircraft where multiple owners share the costs of purchasing, leasing and operating the aircraft.  Commercial programs for large aircraft include NetJets, Flexjet, Flight Options, PlaneSense, Executive AirShare, AirSprint and Autumn Air.

AIDS (aeronautics): AIDS (Aircraft Integrated Data System) is an aircraft system that allows the airline to record and/or monitor all available parameters which are on the aircraft buses.  Some Aircraft like the Airbus A320 have an AIDS print button which, when programmed over the MCDU, allows paper data reports, DAR recordings, or ACARS transmissions of a select amount of parameters to be printed.

Stealth aircraft: Stealth aircraft are designed to avoid detection using a variety of technologies that reduce reflection/emission of radar, infrared, visible light, radio-frequency (RF) spectrum, and audio, collectively known as stealth technology.  Development of stealth technology likely began in Germany during World War II, the prototyped Horten Ho 229 was designed for twin BMW 003 jet engines but finally powered by twin Junkers Jumo 004 jet engines being described as the first stealth aircraft.  Well-known modern examples of stealth of U.S. aircraft include the United States' F-117 Nighthawk (1981–2008), the B-2 Spirit, the F-22 Raptor, and the F-35 Lightning II.

Voyageur Airways: Voyageur Airways Limited is an airline based in North Bay, Ontario, Canada that commenced operations in 1968.  Along with air charters it also repairs and maintains aircraft; and provides an air ambulance service.  It also provides ground handling, fuel services and terminal services at the North Bay/Jack Garland Airport.  It is known to provide chartered aircraft to the United Nations and NATO, for operations in places such as Afghanistan, Democratic Republic of Congo, Chad, Ivory Coast and Sudan.  These aircraft include de Havilland Canada DHC-7 Dash 7 and de Havilland Canada DHC-8 Dash 8 turboprops as well as Bombardier CRJ200 regional jets.

Derelict Aircraft Museum: The Derelict Air Museum is an Australian aviation museum located in Launching Place, Victoria.  It is a collection of aircraft in various states of repair owned by Richard Wetherburn.  The aircraft include a US Air Force North American F-86D Sabre, two Royal Australian Air Force (RAAF) Aermacchi MB-326, a RAAF de Havilland Vampire, a Royal Australian Navy Westland Wessex, a Polish Air Force PZL TS-11 Iskra, a GAF Nomad, a Beechcraft Queen Air, a Commonwealth Department of Health de Havilland Dove and the nose of an Ansett Fokker F-28 Fellowship.  In addition it has a large collection of model aircraft.  As of 2017 it is closed and dismantled.

SS City of Rio de Janeiro: The SS "City of Rio de Janeiro" was an iron-hulled steam-powered passenger ship, launched in 1878, which sailed between San Francisco and various Asian Pacific ports.  On 22 February 1901, the vessel sank after striking a submerged reef at the entry to San Francisco Bay while inward bound from Hong Kong.  Of the approximately 220 passengers and crew on board, fewer than 85 people survived the sinking, while 135 others were killed in the catastrophe.  The wreck lies in 287 ft of water just off the Golden Gate and is listed in the National Register of Historic Places as nationally significant.

Airbus A320 family: The Airbus A320 family consists of short- to medium-range, narrow-body, commercial passenger twin-engine jet airliners manufactured by Airbus.  The family includes the A318, A319, A320 and A321, as well as the ACJ business jet.  The A320s are also named A320ceo (current engine option) after the introduction of the A320neo.  Final assembly of the family takes place in Toulouse, France, and Hamburg, Germany.  A plant in Tianjin, China, has also been producing aircraft for Chinese airlines since 2009, while a final assembly facility in Mobile, Alabama, United States, delivered its first A321 in April 2016.  The aircraft family can accommodate up to 220 passengers and has a range of 3100 to , depending on model.

Military aviation: Military aviation is the use of military aircraft and other flying machines for the purposes of conducting or enabling aerial warfare, including national airlift (air cargo) capacity to provide logistical supply to forces stationed in a theater or along a front.  Airpower includes the national means of conducting such warfare, including the intersection of transport and war craft.  Military aircraft include bombers, fighters, transports, trainer aircraft, and reconnaissance aircraft.

Question: What family of aircraft include an AIDS print button and can accomodate up to 220 passengers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "aircraft_family_name": {
      "type": "string",
      "description": "The name of the aircraft family."
    },
    "features": {
      "type": "array",
      "description": "A list of key features of the aircraft family mentioned in the context.",
      "items": {
        "type": "string"
      }
    },
    "passenger_capacity": {
      "type": "object",
      "properties": {
        "max_passengers": {
          "type": "integer",
          "description": "The maximum number of passengers the aircraft family can accommodate."
        },
        "capacity_unit": {
          "type": "string",
          "description": "The unit for passenger capacity."
        }
      },
      "required": [
        "max_passengers",
        "capacity_unit"
      ],
      "additionalProperties": false
    },
    "system_details": {
      "type": "object",
      "properties": {
        "system_name": {
          "type": "string",
          "description": "The name of the specific aircraft system."
        },
        "functionality": {
          "type": "string",
          "description": "A description of the system's functionality as it relates to the question."
        }
      },
      "required": [
        "system_name",
        "functionality"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "aircraft_family_name",
    "features",
    "passenger_capacity",
    "system_details"
  ],
  "additionalProperties": false
}
