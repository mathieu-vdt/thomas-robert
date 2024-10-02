joueur = Joueur.objects.filter(mail_search=self.email).first()  # type: ignore
pub = get_object_or_404(Pub, id=pub_id) # type: ignore

