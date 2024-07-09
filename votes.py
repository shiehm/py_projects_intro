class Election:
    
    def __init__(self, candidates):
        self.candidate_dict = {}
        for candidate in candidates:
            self.candidate_dict[candidate.name] = candidate.votes
        
    def results(self):
        winner = max(self.candidate_dict, key=lambda k: self.candidate_dict[k])
        percent = max(self.candidate_dict.values()) / sum(self.candidate_dict.values())
        
        for candidate in self.candidate_dict:
            print(f'{candidate}: {self.candidate_dict[candidate]} votes.')
        
        print()
        return f'{winner} won: {percent:.0%} of votes.'

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0
    
    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.votes += other 
        return self

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
print(election.results())

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes


###

# Comparison in ChatGPT between my answer and the book:

# Comparison
# Strengths
# Code 1:
# Simplicity: The Election class directly operates on a list of Candidate objects, making the code straightforward.
# Encapsulation: Candidate objects encapsulate their votes, providing methods to manipulate this data.
# Code 2:
# Efficiency: Uses a dictionary (candidate_dict) to store candidate names and their votes, allowing quick lookups and manipulations.
# Clarity: Separates the candidate data (name and votes) from the election results calculation, potentially making the results method easier to understand.
# Weaknesses
# Code 1:
# Redundant Calculations: The results method iterates over the candidates list twice, once for counting votes and determining the winner, and again for printing results.
# Code Duplication: The same list of candidates is iterated over multiple times, which could be optimized.
# Code 2:
# Data Redundancy: There is a separation between the Candidate class instances and the dictionary in the Election class, which can lead to redundancy and synchronization issues.
# Type Safety: The dictionary relies on string keys for candidate names, which is less robust than directly working with Candidate objects (if names are not unique or are misspelled).
# Conclusion
# Code 1 is more object-oriented, encapsulating data and behavior within classes. However, it can be optimized for performance by reducing redundant iterations.
# Code 2 leverages a dictionary for efficient lookups and simplifies the results method. However, it introduces potential redundancy and synchronization issues between candidate objects and the dictionary.
# The choice between the two approaches can depend on the specific requirements of the application, such as the importance of performance versus code maintainability and clarity.