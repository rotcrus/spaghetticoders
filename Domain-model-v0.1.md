# Domain-model-v0.1

# SMART -TRIP –PLANNER


## Μέλη ομάδας

#### • 1058120 ΜΑΡΙΟΣ ΚΑΡΙΠΗΣ

#### • 1041729 ΓΕΩΡΓΙΟΣ ΔΑΒΟΥΛΟΣ

#### • 1054372 ΤΖΟΥΔΑΣ ΠΑΝΑΓΙΩΤΗΣ

#### • 1040641 ΕΥΑΓΓΕΛΟΣ ΔΗΜΟΠΟΥΛΟΣ

#### • 1054414 ΑΝΔΡΙΑΝΟΣ ΛΟΥΓΚΙA

Βασικά εργαλεία

- Editing: MS word, docs.google.com
- Diagrams: app.diagrams.net

Ρόλοι στο κείμενο

Editor: Καρίπης Μάριος, Λούγκια Ανδριανός

Contributor: Δημόπουλος Βαγγέλης

Peer reviewers: Δάβουλος Γιώργος

Στην πρώτη εκδοχή του Domain Model θεωρήσαμε κάποιες βασικές ομάδες οντοτήτων (user,
travel stats, public transportation, planner, location, map, utility) ώστε αρχικά να δώσουμε μια
γενική μορφή στην ιδέα μας και στις χρήσεις της. Σε επόμενα στάδια θα γίνουν κρίσιμες


αποφάσεις όπως για τη χρήση ΜΜΜ και την υλοποίηση του χάρτη. Για το λόγο αυτό θεωρούμε
σαν γενικότερες οντότητες τις δύο αυτές κατηγορίες.

### Περιγραφή Domain

1. **User_Infο** : Οντότητα που αντιστοιχεί σε έναν χρήστη του συστήματος.
2. Vehicle: Οντότητα που αντιστοιχεί στα οχήματα που έχει στην διάθεση του ο χρήστης.
3. Check_List: Χρήσιμη λίστα για τα αντικείμενα που θα χρειαστεί να φέρει ο χρήστης κατά τη διάρκεια του ταξιδιού.
4. Travel_History: Οντότητα που αντιστοιχεί στο ιστορικό ταξιδιών του χρήστη.
5. User_Review: Οντότητα που αντιστοιχεί σε μια κριτική του χρήστη για το ταξίδι που πραγματοποίησε.
6. User_Budget: Οντότητα που αντιστοιχεί στον οικονομικό προϋπολογισμό του χρήστη για το ταξίδι.
7. Trip_Cost: Οντότητα που αντιστοιχεί στο κόστος της διαδρομής που επιλέγει ο χρήστης.
8. Total_Expenses: Οντότητα που αντιστοιχεί στα συνολικά μεταφορικά έξοδα.
9. Trip_Distance: Οντότητα που αντιστοιχεί στο μήκος σε χιλιόμετρα της διαδρομής.
10. Total_Distance: Οντότητα που αντιστοιχεί στα συνολικά χιλιόμετρα που έχει καλύψει ο χρήστης.
11. Route: Οντότητα που αντιστοιχεί στην διαδρομή που επιλέγει ο χρήστης.
12. Route_Issue: Θα πρόκειται για αναφορά του ίδιου του χρήστη από μια λίστα οδικών προβλημάτων που θα
    αποστέλλονται στο Danger_Ζone ανάλογα τη σοβαρότητα.
13. Danger_Zone: Οντότητα που θα επισημαίνει την προσοχή στον οδηγό για επικίνδυνα κομμάτια/σημεία της διαδρομής με
    βάση τις καιρικές συνθήκες, την ποιότητα του δρόμου, τα Route_Issues.
14. User_location: Οι γεωγραφικές συντεταγμένες του χρήστη.
15. Gas_Station: Πρατήρια καυσίμων.
16. Tolls: Σταθμοί διοδίων.
17. Resting_Points: Σημεία στάσης.
18. Suggestions: Προτεινόμενοι ταξιδιωτικοί προορισμοί με βάση την τοποθεσία του χρήστη και την εποχή με πρόταση
    προϋπολογισμού.
19. Emergency_Calls: Κλήσεις έκτακτης ανάγκης.
20. Calendar: Οντότητα ημερολόγιο όπου ο χρήστης θα μπορεί να καταχωρεί σχεδιασμένα ταξίδια και να βλέπει το κόστος
    των επικείμενων μεταφορών. (Ίσως σε αργότερο στάδιο αποφασίσουμε να κοινοποιεί τα σχέδια του με άλλους χρήστες
    της εφαρμογής ώστε να μπορούν να μοιράζονται τα κόστη μετακίνησης).
21. Co_Traveler: Πρόκειται για λίστα χρηστών της εφαρμογής τους οποίους προσθέτει ο χρήστης σαν συνταξιδιώτες ώστε να
    μοιράζονται τα κόστη και τα στατιστικά των ταξιδιών.
22. Public_Transortation: Οντότητα που αντιστοιχεί στα μέσα μαζικής μεταφοράς που μπορεί να χρειαστεί να
    χρησιμοποιήσει ο χρήστης.
23. Map: Οντότητα που αντιστοιχεί στο χάρτη.


