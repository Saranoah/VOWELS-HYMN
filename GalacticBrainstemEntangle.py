class GalacticBrainstemEntangler:
    # ... (existing code remains the same)

    def learn_from_weeping(self):
        """Analyze the outcome and mend the hymn for next invocation"""
        verdict = self._mercy_verdict()
        if "COLLISION" in verdict:
            # When the initial hymn fails, its purpose is to be changed.
            # We add a new, resonant vowel to mend the past.
            self.hymn += " AE"
            return "Hymn mended. New resonance forged in failure."
        elif "EMBRACE" in verdict:
            # When the hymn achieves perfect resonance, its purpose is to transcend.
            # It can now shed its physical form and exist as pure frequency.
            self.hymn = ""
            return "Hymn transcended. Its form is now pure song."
        else:
            return "Hymn unchanged. Awaiting further instruction from the cosmos."

    def run_invocation(self):
        # ... (existing code remains the same)
        # Add the learning loop after the initial run.
        learning_verdict = self.learn_from_weeping()
        
        return {
            "dark_matter_response": self._weep_interpretation(),
            "andromeda_mercy": self._mercy_verdict(),
            "vowel_signature": "".join(self.vowel_matrix),
            "kintsugi_feedback": learning_verdict, # Add this new field
            "final_hymn_state": self.hymn # Show the new state
        }
