using System.ComponentModel.DataAnnotations;

public class Movie
{
    public int Id { get; set; }

    [Required(ErrorMessage = "Tytuł jest wymagany")]
    public string Title { get; set; }

}