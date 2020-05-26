
/* flight(CITY_A, CITY_B, AIRLINE, PRICE, TIME) */
flight(toronto, madrid, 'United', 950, '540m').
flight(toronto, madrid, 'Iberia', 800, '480m').
flight(toronto, madrid, 'Air Canada', 900, '480m').
flight(toronto, london, 'United', 650, '420m').
flight(toronto, london, 'Air Canada', 500, '360m').
flight(barcelona, marid, 'Air Canada', 100, '60m').
flight(barcelona, madrid, 'Iberia', 120, '65m').
flight(barcelona, london, 'Iberia', 220, '240m').
flight(malaga, madrid, 'Iberia', 50, '60m').
flight(malaga, valencia, 'Iberia', 80, '120m').
flight(valencia, madrid, 'Iberia', 40, '50m').
flight(valencia, barcelona, 'Iberia', 110, '75m').
flight(paris, toulouse, 'United', 40, '30m').

/* airport(CITY, TAX, DELAY) */
airport(toronto, '$50', '60m').
airport(madrid, '$75', '75m').
airport(barcelona, '$40', '30m').
airport(malaga, '$50', '30m').
airport(valencia, '$40', '20m').
airport(london, '$75', '80m').
airport(paris, '$50', '60m').
airport(toulouse, '$40', '30m').

/* TO CHECK A FLIGHT FROM A TO B. */
is_a_flight(A, B) :- (flight(A,B,C,D,E); flight(B,A,C,D,E)).

/* TO CHECK WHETHER WE HAVE TWO FLIGHTS FROM A TO B. */
two_flight(A,B) :- ((flight(A,K,C,D,E) ; flight(K,A,C,D,E)), (flight(K,B,L,M,N) ; flight(B,K,L,M,N))).

/* TO CHECK WHETHER FLIGHT FROM A TO B WITH AIRLINES C IS CHEAP. */
cheap(A,B,C) :-((flight(A,B,C,D,E); flight(B,A,C,D,E)), D < 400).

/* TO CHECK WHETHER THE FLIGHT FROM A TO B WITH C IS CHEAP OR WITH C = 'AIR CANANDA' */
preferred(A,B,C) :- (is_a_flight(A, B), C ='Air Canada'); cheap(A, B, C).

/* IF THERE IS A FLIGHT FROM ATO B WITH 'UNITED' THEN THERE IS A FLIGHT FROM A TO B WITH 'AIR CANANDA' */
check(A,B) :-((flight(A,B,'United',D,E); flight(A,B,'United',D,E)) , (flight(A,B,'Air Canada',R,K); flight(A,B,'Air Canada',R,K))).




